import pandas as pd
import json
import os
from pathlib import Path

def update_video_events(
    video_events_path,
    data_path,
    output_path=None
):
    """
    Update video_events.csv with associatedMedia paths for detections and behavior annotations.

    Args:
        video_events_path: Path to video_events.csv
        data_path: Path to the data directory containing video directories
        output_path: Path to write updated CSV (if None, overwrites input)
    """
    # Read video_events.csv
    df = pd.read_csv(video_events_path)

    # Parse the eventID to extract date and video_id
    # Format: KABR-2023:DATE_SESSION:VIDEO_ID
    for idx, row in df.iterrows():
        event_id = row['eventID']
        parts = event_id.split(':')

        if len(parts) < 3:
            print(f"Warning: Could not parse eventID: {event_id}")
            continue

        date_session = parts[1]
        video_id = parts[2]

        # Extract the date portion (without session)
        # e.g., "11_01_23_session_1" -> "11_01_23"
        date_parts = date_session.split('_session_')
        if len(date_parts) > 1:
            date_part = date_parts[0]
        else:
            date_part = date_session

        # Construct the directory name
        dir_name = f"{date_part}-{video_id}"

        # Build paths to detections and behavior files
        detections_path = os.path.join(data_path, dir_name, "metadata", f"{video_id}_tracks.xml")

        # For behavior annotations, we need to find all XML files in the actions directory
        actions_dir = os.path.join(data_path, dir_name, "actions")
        behavior_files = []

        if os.path.exists(actions_dir):
            behavior_files = [f for f in os.listdir(actions_dir) if f.endswith('.xml')]
            behavior_files.sort()  # Sort for consistency

        # Check if files exist
        detections_exists = os.path.exists(detections_path)

        # Create relative paths from the kabr-behavior-telemetry/data directory
        detections_rel = f"../../../mini-scenes_zebras/kabr-datapalooza-2023/data/{dir_name}/metadata/{video_id}_tracks.xml" if detections_exists else ""

        # Create behavior annotations list with relative paths
        behavior_rel_list = []
        if behavior_files:
            for bf in behavior_files:
                behavior_rel_list.append(f"../../../mini-scenes_zebras/kabr-datapalooza-2023/data/{dir_name}/actions/{bf}")

        # Update the associatedMedia field with JSON structure
        associated_media = {
            "detection": detections_rel,
            "behavior": behavior_rel_list
        }

        # Update the dataframe
        df.at[idx, 'associatedMedia'] = json.dumps(associated_media)

        # Print status
        status = "✓" if detections_exists else "✗"
        behavior_count = len(behavior_files) if behavior_files else 0
        print(f"{status} {video_id}: detections={detections_exists}, behaviors={behavior_count}")

    # Write the updated CSV
    if output_path is None:
        output_path = video_events_path

    df.to_csv(output_path, index=False)
    print(f"\nUpdated video_events.csv written to: {output_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Update video_events.csv with associatedMedia paths")
    parser.add_argument(
        "--video_events",
        type=str,
        required=True,
        help="Path to video_events.csv"
    )
    parser.add_argument(
        "--data_path",
        type=str,
        required=True,
        help="Path to data directory containing video directories"
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output path (default: overwrites input)"
    )

    args = parser.parse_args()

    update_video_events(
        args.video_events,
        args.data_path,
        args.output
    )
