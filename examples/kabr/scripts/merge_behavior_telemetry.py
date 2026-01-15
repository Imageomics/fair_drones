import re
import os
import json
import pysrt
import argparse
import pandas as pd
from tqdm import tqdm
from glob import glob
from datetime import datetime
import xml.etree.ElementTree as ET

" Based on script authored by Otto Brookes for KABR-2023 project "


def pandify_xml_tracks(path2tracks):
    elems = []
    et = ET.parse(path2tracks)
    root = et.getroot()
    for row in root:
        for e in row.iter("box"):
            for k, v in row.attrib.items():
                e.attrib[k] = v
            elems.append(e.attrib)
    track_df = pd.DataFrame(elems)
    track_df["frame"] = track_df.frame.astype(int)
    return track_df


def extract_frame_no(text):
    pattern = r": (\d+),"
    matches = re.findall(pattern, text)
    numbers = [int(match) for match in matches]
    assert len(numbers) == 1, "Frame index must be unique"
    return next(iter(numbers))


def extract_meta_data(text):
    # Extract all [text]
    pattern = r"\[(.*?)\]"
    matches = re.findall(pattern, text)
    data_dict = {}
    for item in matches:
        key_value = item.split(":", 1)
        key = key_value[0].strip()
        value = key_value[1].strip()
        data_dict[key] = value
    return data_dict


def pandify_srt_data(path2srt):
    subs = pysrt.open(path2srt)
    all_meta_data = []
    for s in subs:
        split_text = s.text.split("\n")
        meta_data = extract_meta_data(split_text[2])
        meta_data["frame"] = extract_frame_no(split_text[0])
        meta_data["date_time"] = split_text[1]
        all_meta_data.append(meta_data)
    srt_df = pd.DataFrame(all_meta_data)
    srt_df["frame"] = srt_df["frame"] - 1
    return srt_df


def get_per_frame_annotations(path2xml):
    et = ET.parse(path2xml)
    root = et.getroot()
    per_frame_annotations = []
    for row in root.findall("track"):
        for e, j in zip(row.iter("points"), row.iter("attribute")):
            behaviour = j.text
            e.attrib["behaviour"] = behaviour
            per_frame_annotations.append(e.attrib)
    return per_frame_annotations


def add_per_frame_behaviours(merged_df, path2annotations):
    mini_scenes_df = None
    ms_annotations = glob(f"{path2annotations}/**/*.xml", recursive=True)
    for ms in ms_annotations:
        ms_index = ms.split("/")[-1].split(".")[0]
        ms_df = merged_df[merged_df.id == str(ms_index)].sort_values(by="frame")
        first_frame = ms_df.frame.iloc[0]  # ugly - rework later
        per_frame_anns = pd.DataFrame(get_per_frame_annotations(ms))
        per_frame_anns["frame"] = per_frame_anns.frame.astype(int) + first_frame
        ms_df = ms_df.merge(per_frame_anns, on="frame")
        if mini_scenes_df is None:
            mini_scenes_df = ms_df
        else:
            mini_scenes_df = pd.concat([mini_scenes_df, ms_df])
    return mini_scenes_df


def find_srt_file(session_data_root, date_part, filename):
    """
    Recursively search for SRT file matching the date and filename.

    Args:
        session_data_root: Root path to session_data directory
        date_part: Date portion of the directory name (e.g., '11_01_23' or '17_01_2023_session_1')
        filename: DJI filename (e.g., 'DJI_0488')

    Returns:
        Path to SRT file if found, None otherwise
    """
    # Try to find the date directory in session_data
    date_dir = os.path.join(session_data_root, date_part)
    if not os.path.exists(date_dir):
        # Try without session suffix for cases like '16_01_23_session_1' -> '16_01_23'
        base_date = date_part.split('_session_')[0]
        date_dir = os.path.join(session_data_root, base_date)

    if not os.path.exists(date_dir):
        print(f"Warning: Could not find date directory for {date_part}")
        return None

    # Recursively search for the SRT file
    srt_filename = f"{filename}.SRT"
    for root, dirs, files in os.walk(date_dir):
        if srt_filename in files:
            return os.path.join(root, srt_filename)

    return None


def find_flight_log(flight_logs_path, srt_df):
    """
    Find the matching flight log CSV based on datetime from SRT data.

    Args:
        flight_logs_path: Path to decrypted_flight_logs directory
        srt_df: DataFrame with SRT data containing date_time column

    Returns:
        Path to matching flight log CSV, or None if not found
    """
    if srt_df.empty or 'date_time' not in srt_df.columns:
        return None

    # Get first datetime from SRT (format: "2023-01-11 16:04:03,681,492")
    first_datetime_str = srt_df['date_time'].iloc[0]
    # Parse just the date and time part (ignore milliseconds)
    srt_datetime = datetime.strptime(first_datetime_str.split(',')[0], "%Y-%m-%d %H:%M:%S")

    # Search for matching flight log
    flight_logs = glob(f"{flight_logs_path}/*.csv")

    for log_path in flight_logs:
        # Read full file to get complete time range (many files are small)
        try:
            log_df = pd.read_csv(log_path)
            if 'datetime(utc)' not in log_df.columns or log_df.empty:
                continue

            # Convert to datetime and add 3 hours (flight logs are 3 hours behind)
            log_df['datetime_corrected'] = pd.to_datetime(log_df['datetime(utc)']) + pd.Timedelta(hours=3)

            # Check if SRT datetime falls within flight log timerange
            log_start = log_df['datetime_corrected'].min()
            log_end = log_df['datetime_corrected'].max()

            # Skip if dates are invalid
            if pd.isna(log_start) or pd.isna(log_end):
                continue

            if log_start <= srt_datetime <= log_end:
                return log_path
        except Exception as e:
            continue

    return None


def merge_flight_log_data(merged_df, flight_log_path):
    """
    Merge flight log data with the main dataframe based on datetime.

    Args:
        merged_df: Main dataframe with date_time column
        flight_log_path: Path to flight log CSV

    Returns:
        Merged dataframe with flight log data
    """
    if flight_log_path is None or not os.path.exists(flight_log_path):
        return merged_df

    try:
        # Read flight log
        flight_df = pd.read_csv(flight_log_path)

        # Prepare datetime columns for merging
        # SRT format: "2023-01-11 16:04:03,681,492" -> convert to "2023-01-11 16:04:03"
        merged_df['datetime_merge'] = merged_df['date_time'].apply(
            lambda x: x.split(',')[0] if pd.notna(x) else None
        )

        # Flight log format: "2023-01-11 07:45:46"
        # IMPORTANT: Flight log datetimes are 3 hours behind actual time - add 3 hours
        flight_df['datetime_merge'] = pd.to_datetime(flight_df['datetime(utc)']) + pd.Timedelta(hours=3)

        # Merge on datetime
        merged_df['datetime_merge'] = pd.to_datetime(merged_df['datetime_merge'])

        # Use merge_asof for nearest time matching
        merged_df = merged_df.sort_values('datetime_merge')
        flight_df = flight_df.sort_values('datetime_merge')

        # Merge with flight log data
        result_df = pd.merge_asof(
            merged_df,
            flight_df,
            on='datetime_merge',
            direction='nearest',
            tolerance=pd.Timedelta('2s'),  # Increased tolerance to 2 seconds
            suffixes=('', '_flight')
        )

        # Drop temporary merge column and handle duplicate columns
        result_df = result_df.drop('datetime_merge', axis=1)

        # Remove duplicate latitude/longitude/altitude columns from flight log if they exist
        # Keep the SRT versions (more accurate for video frames)
        for col in ['latitude', 'longitude', 'altitude']:
            if f'{col}_flight' in result_df.columns:
                result_df = result_df.drop(f'{col}_flight', axis=1)

        print(f"  Merged with flight log: {os.path.basename(flight_log_path)}")
        return result_df

    except Exception as e:
        print(f"  Warning: Could not merge flight log: {str(e)}")
        if 'datetime_merge' in merged_df.columns:
            merged_df = merged_df.drop('datetime_merge', axis=1)
        return merged_df


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data_path",
        type=str,
        help="Please use the full path to the data dir in this repo!",
    )
    parser.add_argument(
        "--session_data_path",
        type=str,
        default="/fs/ess/PAS2136/Kenya-2023/Zebras/session_data",
        help="Path to session_data directory containing SRT files",
    )
    parser.add_argument(
        "--flight_logs_path",
        type=str,
        default="/fs/ess/PAS2136/Kenya-2023/Zebras/Flight_Logs/decrypted_flight_logs",
        help="Path to decrypted_flight_logs directory",
    )
    parser.add_argument(
        "--skip-airdata",
        action="store_true",
        help="Skip merging with airdata/flight log files",
    )
    parser.add_argument("--write", type=bool, default=True)
    parser.add_argument("--outpath", type=str, help="Path to write csvs to")
    args = parser.parse_args()

    path2data = args.data_path
    session_data_root = args.session_data_path
    flight_logs_path = args.flight_logs_path
    data_dirs = [x for x in os.listdir(path2data) if not x.startswith(".")]
    path2write = args.outpath

    good = 0
    fail = 0
    failed_files = []

    for d in tqdm(data_dirs):
        try:
            # Parse directory name to get date and filename
            # Format: DATE-FILENAME (e.g., '11_01_23-DJI_0488' or '17_01_2023_session_1-DJI_0005')
            parts = d.split("-")
            date_part = parts[0]
            filename = parts[-1]

            # Formulate paths
            path2tracks = f"{path2data}/{d}/metadata/{filename}_tracks.xml"
            path2annotations = f"{path2data}/{d}/actions/"

            # Find SRT file recursively
            path2srt = find_srt_file(session_data_root, date_part, filename)

            if path2srt is None:
                raise FileNotFoundError(f"Could not find SRT file for {date_part}-{filename}")

            print(f"Processing {d}: Found SRT at {path2srt}")

            # initialise dfs:
            srt_df = pandify_srt_data(path2srt)
            track_df = pandify_xml_tracks(path2tracks)
            merged_df = srt_df.merge(track_df, on="frame", how="left")

            # Add date and video_id columns to ALL rows
            merged_df.insert(0, "date", date_part)
            merged_df.insert(1, "video_id", filename)

            # Move frame to position 2
            frame_col = merged_df.pop("frame")
            merged_df.insert(2, "frame", frame_col)

            # Move id (mini-scene id) to position 3
            if "id" in merged_df.columns:
                id_col = merged_df.pop("id")
                merged_df.insert(3, "id", id_col)

            # Ensure date_time is preserved (move to position 4)
            if "date_time" in merged_df.columns:
                datetime_col = merged_df.pop("date_time")
                merged_df.insert(4, "date_time", datetime_col)

            # Find and merge flight log data if path provided and not skipped
            if flight_logs_path and not args.skip_airdata:
                flight_log_path = find_flight_log(flight_logs_path, srt_df)
                if flight_log_path:
                    merged_df = merge_flight_log_data(merged_df, flight_log_path)

            # Add per frame behaviours to existing df
            mini_scene_df = add_per_frame_behaviours(merged_df, path2annotations)

            # Merge with frame df to preserve all frames (including those without annotations)
            frame_df = merged_df[['date', 'video_id', 'frame', 'date_time']]
            mini_scene_df = frame_df.merge(
                mini_scene_df, on="frame", how="left"
            )

            # Remove duplicate date/video_id columns if they exist
            for col in ['date_x', 'date_y', 'video_id_x', 'video_id_y', 'date_time_x', 'date_time_y']:
                if col in mini_scene_df.columns:
                    # Keep the non-null version
                    base_col = col.rsplit('_', 1)[0]
                    if f'{base_col}_x' in mini_scene_df.columns and f'{base_col}_y' in mini_scene_df.columns:
                        mini_scene_df[base_col] = mini_scene_df[f'{base_col}_x'].fillna(mini_scene_df[f'{base_col}_y'])
                        mini_scene_df = mini_scene_df.drop([f'{base_col}_x', f'{base_col}_y'], axis=1)

            if args.write:
                mini_scene_df.sort_values(by="frame").to_csv(path2write+f"{d}.csv", index=False)
            good += 1
        except Exception as e:
            failed_files.append(d)
            print(f"Failed on {d}: {str(e)}")
            fail += 1
    print("Pass: ", good, "Fail: ", fail)
    print("Failed files:", failed_files)

if __name__ == "__main__":
    main()