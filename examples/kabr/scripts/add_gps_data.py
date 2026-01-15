import pandas as pd
import numpy as np
import os
import json

def extract_gps_from_occurrence(occurrence_path):
    """
    Extract GPS statistics from an occurrence file.

    Returns:
        dict with keys: launch_lat, launch_lon, min_lat, max_lat, min_lon, max_lon, min_alt, max_alt
    """
    try:
        # Read occurrence file with low_memory=False to avoid dtype warnings
        occ_df = pd.read_csv(occurrence_path, low_memory=False)

        if occ_df.empty:
            return None

        # Get GPS columns
        lat_col = occ_df['latitude'].dropna()
        lon_col = occ_df['longitude'].dropna()
        alt_col = occ_df['altitude'].dropna()

        if lat_col.empty or lon_col.empty:
            return None

        # Launch point is the first GPS coordinate
        launch_lat = float(lat_col.iloc[0])
        launch_lon = float(lon_col.iloc[0])

        # Calculate min/max
        stats = {
            'launch_lat': launch_lat,
            'launch_lon': launch_lon,
            'min_lat': float(lat_col.min()),
            'max_lat': float(lat_col.max()),
            'min_lon': float(lon_col.min()),
            'max_lon': float(lon_col.max()),
        }

        # Add altitude if available
        if not alt_col.empty:
            stats['min_alt'] = float(alt_col.min())
            stats['max_alt'] = float(alt_col.max())
        else:
            stats['min_alt'] = None
            stats['max_alt'] = None

        return stats

    except Exception as e:
        print(f"Error processing {occurrence_path}: {str(e)}")
        return None


def add_gps_to_video_events(video_events_path, occurrences_path, output_path=None):
    """
    Add GPS columns to video_events.csv from occurrence files.

    Adds columns:
    - decimalLatitude (launch point)
    - decimalLongitude (launch point)
    - minimumElevationInMeters
    - maximumElevationInMeters
    - footprintWKT (bounding box in WKT format)
    """
    # Read video_events.csv
    df = pd.read_csv(video_events_path)

    # Add new columns if they don't exist
    new_columns = ['decimalLatitude', 'decimalLongitude',
                   'minimumElevationInMeters', 'maximumElevationInMeters',
                   'footprintWKT']

    for col in new_columns:
        if col not in df.columns:
            df[col] = np.nan

    # Process each video
    for idx, row in df.iterrows():
        event_id = row['eventID']
        parts = event_id.split(':')

        if len(parts) < 3:
            continue

        date_session = parts[1]
        video_id = parts[2]

        # Extract the date portion
        date_parts = date_session.split('_session_')
        date_part = date_parts[0] if len(date_parts) > 1 else date_session

        # Construct occurrence filename
        # Try with underscore first (for flight_1, flight_2 format)
        occurrence_file = f"{date_part}_{video_id}.csv"
        occurrence_path = os.path.join(occurrences_path, occurrence_file)

        # If that doesn't exist, try with dash (for older format)
        if not os.path.exists(occurrence_path):
            occurrence_file = f"{date_part}-{video_id}.csv"
            occurrence_path = os.path.join(occurrences_path, occurrence_file)

        if not os.path.exists(occurrence_path):
            print(f"⚠ {video_id}: No occurrence file")
            continue

        # Extract GPS data
        gps_stats = extract_gps_from_occurrence(occurrence_path)

        if gps_stats is None:
            print(f"⚠ {video_id}: No GPS data")
            continue

        # Update video_events
        df.at[idx, 'decimalLatitude'] = gps_stats['launch_lat']
        df.at[idx, 'decimalLongitude'] = gps_stats['launch_lon']

        if gps_stats['min_alt'] is not None:
            df.at[idx, 'minimumElevationInMeters'] = gps_stats['min_alt']
            df.at[idx, 'maximumElevationInMeters'] = gps_stats['max_alt']

        # Create WKT footprint (bounding box)
        wkt = f"POLYGON(({gps_stats['min_lon']} {gps_stats['min_lat']}, " \
              f"{gps_stats['max_lon']} {gps_stats['min_lat']}, " \
              f"{gps_stats['max_lon']} {gps_stats['max_lat']}, " \
              f"{gps_stats['min_lon']} {gps_stats['max_lat']}, " \
              f"{gps_stats['min_lon']} {gps_stats['min_lat']}))"
        df.at[idx, 'footprintWKT'] = wkt

        print(f"✓ {video_id}: Launch ({gps_stats['launch_lat']:.6f}, {gps_stats['launch_lon']:.6f}), "
              f"Bounds: lat[{gps_stats['min_lat']:.6f}, {gps_stats['max_lat']:.6f}], "
              f"lon[{gps_stats['min_lon']:.6f}, {gps_stats['max_lon']:.6f}]")

    # Write updated CSV
    if output_path is None:
        output_path = video_events_path

    df.to_csv(output_path, index=False)
    print(f"\nUpdated video_events.csv written to: {output_path}")
    return df


def add_gps_to_session_events(session_events_path, video_events_df, output_path=None):
    """
    Add GPS columns to session_events.csv by aggregating from video_events.

    For each session:
    - launchLatitude/launchLongitude: Launch point of first video in session
    - decimalLatitude: [min, max] latitude range as string
    - decimalLongitude: [min, max] longitude range as string
    - footprintWKT: Bounding box encompassing all videos in session
    - minimumElevationInMeters/maximumElevationInMeters: Min/max across all videos
    """
    # Read session_events.csv
    session_df = pd.read_csv(session_events_path)

    # Add new columns if they don't exist
    new_columns = ['launchLatitude', 'launchLongitude',
                   'minimumElevationInMeters', 'maximumElevationInMeters',
                   'footprintWKT']

    for col in new_columns:
        if col not in session_df.columns:
            session_df[col] = np.nan

    # Process each session
    for idx, row in session_df.iterrows():
        session_id = row['eventID']

        # Get all videos for this session
        session_videos = video_events_df[video_events_df['parentEventID'] == session_id]

        if session_videos.empty:
            print(f"⚠ {session_id}: No videos found")
            continue

        # Filter videos with GPS data
        videos_with_gps = session_videos.dropna(subset=['decimalLatitude', 'decimalLongitude'])

        if videos_with_gps.empty:
            print(f"⚠ {session_id}: No GPS data in videos")
            continue

        # Launch point from first video
        first_video = videos_with_gps.iloc[0]
        session_df.at[idx, 'launchLatitude'] = first_video['decimalLatitude']
        session_df.at[idx, 'launchLongitude'] = first_video['decimalLongitude']

        # Calculate session-level min/max across all videos
        min_lat = videos_with_gps['decimalLatitude'].min()
        max_lat = videos_with_gps['decimalLatitude'].max()
        min_lon = videos_with_gps['decimalLongitude'].min()
        max_lon = videos_with_gps['decimalLongitude'].max()

        # Set decimalLatitude and decimalLongitude to [min, max] ranges
        session_df.at[idx, 'decimalLatitude'] = f"[{min_lat:.6f}, {max_lat:.6f}]"
        session_df.at[idx, 'decimalLongitude'] = f"[{min_lon:.6f}, {max_lon:.6f}]"

        # Aggregate elevation
        if 'minimumElevationInMeters' in videos_with_gps.columns:
            elev_videos = videos_with_gps.dropna(subset=['minimumElevationInMeters'])
            if not elev_videos.empty:
                session_df.at[idx, 'minimumElevationInMeters'] = elev_videos['minimumElevationInMeters'].min()
                session_df.at[idx, 'maximumElevationInMeters'] = elev_videos['maximumElevationInMeters'].max()

        # Create session footprint
        wkt = f"POLYGON(({min_lon} {min_lat}, {max_lon} {min_lat}, " \
              f"{max_lon} {max_lat}, {min_lon} {max_lat}, {min_lon} {min_lat}))"
        session_df.at[idx, 'footprintWKT'] = wkt

        print(f"✓ {session_id.split(':')[1]}: Launch ({first_video['decimalLatitude']:.6f}, {first_video['decimalLongitude']:.6f}), "
              f"Session bounds: lat[{min_lat:.6f}, {max_lat:.6f}], lon[{min_lon:.6f}, {max_lon:.6f}]")

    # Write updated CSV
    if output_path is None:
        output_path = session_events_path

    session_df.to_csv(output_path, index=False)
    print(f"\nUpdated session_events.csv written to: {output_path}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Add GPS data to video_events and session_events")
    parser.add_argument("--video_events", type=str, required=True, help="Path to video_events.csv")
    parser.add_argument("--session_events", type=str, required=True, help="Path to session_events.csv")
    parser.add_argument("--occurrences", type=str, required=True, help="Path to occurrences directory")
    parser.add_argument("--output_video", type=str, default=None, help="Output path for video_events (default: overwrite)")
    parser.add_argument("--output_session", type=str, default=None, help="Output path for session_events (default: overwrite)")

    args = parser.parse_args()

    print("=" * 80)
    print("STEP 1: Adding GPS data to video_events.csv")
    print("=" * 80)
    video_df = add_gps_to_video_events(args.video_events, args.occurrences, args.output_video)

    print("\n" + "=" * 80)
    print("STEP 2: Adding GPS data to session_events.csv")
    print("=" * 80)
    add_gps_to_session_events(args.session_events, video_df, args.output_session)

    print("\n" + "=" * 80)
    print("DONE!")
    print("=" * 80)


if __name__ == "__main__":
    main()
