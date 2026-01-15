import pandas as pd
import os
from datetime import datetime

def add_event_times(
    video_events_path,
    occurrences_path,
    output_path=None
):
    """
    Update video_events.csv with eventTime and endTime from occurrence files.

    Args:
        video_events_path: Path to video_events.csv
        occurrences_path: Path to occurrences directory
        output_path: Path to write updated CSV (if None, overwrites input)
    """
    # Read video_events.csv
    df = pd.read_csv(video_events_path)

    # Parse the eventID to extract video_id
    for idx, row in df.iterrows():
        event_id = row['eventID']
        parts = event_id.split(':')

        if len(parts) < 3:
            print(f"Warning: Could not parse eventID: {event_id}")
            continue

        date_session = parts[1]
        video_id = parts[2]

        # Extract the date portion (without session)
        date_parts = date_session.split('_session_')
        if len(date_parts) > 1:
            date_part = date_parts[0]
        else:
            date_part = date_session

        # Construct the occurrence filename
        occurrence_file = f"{date_part}-{video_id}.csv"
        occurrence_path = os.path.join(occurrences_path, occurrence_file)

        if not os.path.exists(occurrence_path):
            print(f"⚠ {video_id}: No occurrence file found")
            continue

        try:
            # Read the occurrence file
            occ_df = pd.read_csv(occurrence_path)

            if 'date_time' not in occ_df.columns or occ_df.empty:
                print(f"⚠ {video_id}: No date_time data")
                continue

            # Get first and last non-null date_time values
            date_times = occ_df['date_time'].dropna()

            if date_times.empty:
                print(f"⚠ {video_id}: All date_time values are null")
                continue

            # Extract the first and last timestamps
            # Format: "2023-01-11 16:04:03,114,286"
            first_dt_str = str(date_times.iloc[0])
            last_dt_str = str(date_times.iloc[-1])

            # Parse to extract just the time portion (HH:MM:SS)
            first_time = first_dt_str.split(',')[0].split(' ')[1] if ' ' in first_dt_str else None
            last_time = last_dt_str.split(',')[0].split(' ')[1] if ' ' in last_dt_str else None

            if first_time and last_time:
                # Update the dataframe
                df.at[idx, 'eventTime'] = first_time
                df.at[idx, 'endTime'] = last_time
                print(f"✓ {video_id}: {first_time} - {last_time}")
            else:
                print(f"⚠ {video_id}: Could not parse time")

        except Exception as e:
            print(f"✗ {video_id}: Error - {str(e)}")

    # Write the updated CSV
    if output_path is None:
        output_path = video_events_path

    df.to_csv(output_path, index=False)
    print(f"\nUpdated video_events.csv written to: {output_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Add event times to video_events.csv from occurrence files")
    parser.add_argument(
        "--video_events",
        type=str,
        required=True,
        help="Path to video_events.csv"
    )
    parser.add_argument(
        "--occurrences",
        type=str,
        required=True,
        help="Path to occurrences directory"
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output path (default: overwrites input)"
    )

    args = parser.parse_args()

    add_event_times(
        args.video_events,
        args.occurrences,
        args.output
    )
