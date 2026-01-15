# KABR Behavior Telemetry Example

This example demonstrates how to create a WildFAIRx-compliant dataset from drone wildlife monitoring data. It showcases the complete workflow for transforming raw drone footage, GPS telemetry, and behavior annotations into a structured, machine-readable dataset that follows FAIR principles and biodiversity data standards.

## What This Example Contains

This is a **reference implementation** showing how the [KABR Behavior Telemetry dataset](https://huggingface.co/datasets/imageomics/kabr-behavior-telemetry) was created from drone monitoring of wildlife in Kenya. It includes:

### 1. WildFAIRx-Compliant Dataset Card ([dataset_card.md](dataset_card.md))
A complete dataset card demonstrating how to:
- Structure metadata following WildFAIRx (FAIR + AI-Ready) principles
- Implement Darwin Core Event standards for wildlife observations
- Document drone sensor specifications and camera settings
- Provide comprehensive provenance and licensing information
- Enable both human readability and machine parsing

### 2. Data Processing Scripts ([scripts/](scripts/))

These Python scripts demonstrate the complete data preparation pipeline, showing how to transform raw drone data into WildFAIRx-compliant datasets:

#### **[merge_behavior_telemetry.py](scripts/merge_behavior_telemetry.py)** - Main Pipeline Script
**What it does:**
- Combines four data sources into unified frame-level occurrence records:
  1. **Drone telemetry** from SRT files (GPS coordinates, altitude)
  2. **Camera metadata** from SRT files (ISO, shutter speed, focal length, etc.)
  3. **Object detection tracks** from XML files (bounding boxes, species IDs)
  4. **Behavior annotations** from XML files (grazing, walking, running, etc.)
- Creates one CSV file per video with every frame linked to its spatial, temporal, and behavioral data

**Input files:**
- `*.SRT` - Drone telemetry files (GPS + camera settings per frame)
- `*_tracks.xml` - Object detection/tracking annotations
- `actions/*.xml` - Behavior annotations for tracked animals

**Output:**
- `data/occurrences/{date}-{video_id}.csv` - Frame-level occurrence records

**Example usage:**
```bash
python scripts/merge_behavior_telemetry.py \
  --session_data /path/to/raw/drone/data \
  --annotations /path/to/behavior/annotations \
  --output_dir ./data/occurrences
```

#### **[add_gps_data.py](scripts/add_gps_data.py)** - Event-Level GPS Enrichment
**What it does:**
- Reads the frame-level occurrence files and computes summary GPS statistics for each video event
- Adds Darwin Core spatial fields to `video_events.csv`:
  - `decimalLatitude` / `decimalLongitude` (launch point coordinates)
  - `minimumElevationInMeters` / `maximumElevationInMeters` (altitude range)
  - `footprintWKT` (bounding box in Well-Known Text format for GIS compatibility)

**Why this matters:** Event-level GPS summaries enable spatial queries and geographic filtering without loading frame-level data

**Example usage:**
```bash
python scripts/add_gps_data.py \
  --video_events ./data/video_events.csv \
  --occurrences ./data/occurrences \
  --output ./data/video_events_with_gps.csv
```

#### **[add_event_times.py](scripts/add_event_times.py)** - Temporal Metadata Extraction
**What it does:**
- Extracts start and end timestamps from frame-level occurrence files
- Updates `video_events.csv` with Darwin Core temporal fields:
  - `eventTime` (start time of video in HH:MM:SS format)
  - `endTime` (end time of video)

**Why this matters:** Enables temporal filtering and analysis of daily activity patterns, time-of-day behaviors, etc.

**Example usage:**
```bash
python scripts/add_event_times.py \
  --video_events ./data/video_events.csv \
  --occurrences ./data/occurrences
```

#### **[update_video_events.py](scripts/update_video_events.py)** - Source File Linkage
**What it does:**
- Links each video event to its source annotation files
- Updates `associatedMedia` field in `video_events.csv` with JSON containing:
  - Path to detection XML file
  - List of paths to behavior annotation XML files
- Validates that referenced files exist

**Why this matters:** Maintains data provenance and enables users to trace processed data back to original source files

**Example usage:**
```bash
python scripts/update_video_events.py \
  --video_events ./data/video_events.csv \
  --data_path /path/to/raw/data
```

### 3. Metadata Documentation ([metadata/](metadata/))
- **[DATA_DICTIONARY.md](metadata/DATA_DICTIONARY.md)**: Comprehensive field-level documentation for all data files, explaining every column in the occurrence records
- **[event_session_fields.csv](metadata/event_session_fields.csv)**: Darwin Core Event field mappings showing how the dataset conforms to biodiversity standards

## Data Pipeline Overview

This example demonstrates how raw drone data flows through a processing pipeline to create AI-ready datasets:

```
Raw Drone Data                    Processing Scripts              Output Dataset
───────────────                    ──────────────────              ──────────────

📹 Video Files (*.MP4)
📍 GPS Telemetry (*.SRT)      ──┐
📷 Camera Metadata (*.SRT)      ├──► merge_behavior_         ──► 📊 Frame-level
🎯 Detection Tracks (*.xml)   ──┤    telemetry.py                  Occurrences
🐾 Behavior Labels (*.xml)    ──┘                                  (CSV files)
                                                                         │
                                                                         │
                               ┌─────────────────────────────────────────┘
                               │
                               ├──► add_gps_data.py         ──► 🗺️  Event GPS
                               │                                  Summaries
                               │
                               ├──► add_event_times.py      ──► ⏰ Event Time
                               │                                  Windows
                               │
                               └──► update_video_events.py  ──► 🔗 Source File
                                                                  Provenance

Final Output: WildFAIRx-compliant dataset ready for Hugging Face
```

## Prerequisites

**For using the dataset:** No prerequisites - just install the Hugging Face datasets library:
```bash
pip install datasets
```

**For running the processing scripts:** You'll need:
```bash
pip install pandas numpy pysrt tqdm
```

Your raw drone data should include:
- DJI drone video files (MP4 format)
- SRT telemetry files (GPS + camera metadata, auto-generated by DJI drones)
- Object detection annotations (CVAT XML format or similar)
- Behavior annotations (frame-level labels in XML format)

## Getting Started

### For Dataset Users
If you just want to **use** the dataset for machine learning or analysis:

```python
from datasets import load_dataset

# Load the complete dataset
dataset = load_dataset("imageomics/kabr-behavior-telemetry")

# Access frame-level occurrence data
occurrences = dataset['train']  # Contains all frame-level records

# Each record contains:
# - GPS coordinates (latitude, longitude, altitude)
# - Camera settings (ISO, shutter, focal_len, etc.)
# - Animal detections (bounding boxes, species)
# - Behavior labels (grazing, walking, running, etc.)
# - Timestamps and frame numbers
```

### For Dataset Creators
If you want to **create your own** WildFAIRx-compliant drone dataset:

1. **Study the dataset card** ([dataset_card.md](dataset_card.md)) to understand the metadata structure
2. **Examine the data dictionary** ([metadata/DATA_DICTIONARY.md](metadata/DATA_DICTIONARY.md)) to see field definitions
3. **Review the processing scripts** ([scripts/](scripts/)) to understand the data pipeline
4. **Adapt the scripts** for your own drone data sources

**Typical workflow:**
```bash
# Step 1: Merge all data sources into frame-level occurrences
python scripts/merge_behavior_telemetry.py --session_data ./raw_data --output_dir ./occurrences

# Step 2: Add GPS summaries to video events
python scripts/add_gps_data.py --video_events ./video_events.csv --occurrences ./occurrences

# Step 3: Add temporal metadata
python scripts/add_event_times.py --video_events ./video_events.csv --occurrences ./occurrences

# Step 4: Link to source files
python scripts/update_video_events.py --video_events ./video_events.csv --data_path ./raw_data
```

## What You'll Learn

This example illustrates:
- How to combine **multiple data sources** (drone GPS, camera telemetry, object detection, behavior annotations) into a unified dataset
- How to structure **frame-level occurrence records** that link every video frame to its spatial coordinates, camera settings, and observed behaviors
- How to create **Darwin Core-compliant** wildlife observation data
- How to document datasets for **reproducibility** and **reusability** in AI/ML research
- How to apply **WildFAIRx principles** to drone-based wildlife monitoring data
- How to handle **heterogeneous data formats** (SRT telemetry, XML annotations, video metadata)

## Using the Dataset

The resulting dataset is publicly available on Hugging Face:

```python
from datasets import load_dataset
dataset = load_dataset("imageomics/kabr-behavior-telemetry")
```

The dataset provides frame-level records combining:
- Animal detections (bounding boxes, species)
- Behavior annotations (grazing, walking, running, etc.)
- GPS coordinates for each frame
- Camera metadata (ISO, shutter speed, focal length, etc.)
- Temporal information (timestamps, video frame numbers)

## Directory Structure

```
examples/kabr/
├── README.md                          # This file
├── dataset_card.md                    # WildFAIRx-compliant dataset documentation
├── metadata/
│   ├── DATA_DICTIONARY.md            # Field-level documentation
│   └── event_session_fields.csv      # Darwin Core Event mappings
└── scripts/
    ├── merge_behavior_telemetry.py   # Main data pipeline script
    ├── add_gps_data.py               # GPS telemetry integration
    ├── add_event_times.py            # Timestamp processing
    └── update_video_events.py        # Annotation validation
```

## Common Questions

**Q: Do I need the raw video files to use the dataset?**
A: No. The dataset contains frame-level occurrence records with all extracted metadata. Videos are not included due to size constraints, but GPS coordinates and timestamps allow you to recreate spatial-temporal context.

**Q: Can I use these scripts with non-DJI drones?**
A: Yes, but you'll need to modify the telemetry parsing. The `merge_behavior_telemetry.py` script reads DJI's SRT format. For other drones, adapt the `pandify_srt_data()` function to parse your drone's telemetry format.

**Q: What if I only have object detections but no behavior annotations?**
A: You can still use the pipeline! The scripts will create occurrence records with detection data only. Behavior fields will be empty but the spatial-temporal framework remains valid.

**Q: How do I know if my dataset is WildFAIRx compliant?**
A: Use the [dataset_card.md](dataset_card.md) as a checklist. Key requirements:
- ✓ Darwin Core Event fields for spatial-temporal data
- ✓ Machine-readable metadata (CSV, JSON)
- ✓ Clear license (CC0, CC-BY, etc.)
- ✓ Documented provenance (data sources, processing steps)
- ✓ Field-level documentation (data dictionary)

**Q: Can I contribute improvements to these scripts?**
A: Yes! This is a reference implementation. Contributions that improve generalizability, add support for other drone platforms, or enhance Darwin Core compliance are welcome.

## Troubleshooting

**"Could not parse eventID" errors:**
- Check that your `video_events.csv` uses the format: `KABR-2023:DATE_SESSION:VIDEO_ID`
- Example: `KABR-2023:11_01_23_session_1:DJI_0977`

**"No occurrence file found" warnings:**
- Verify that occurrence filenames match the pattern: `{date}-{video_id}.csv`
- Example: `11_01_23-DJI_0977.csv`

**Empty GPS or timestamp fields:**
- Ensure your SRT files are properly formatted and contain telemetry data
- Check that SRT files are named identically to video files (e.g., `DJI_0977.SRT` for `DJI_0977.MP4`)

**Script fails with "No module named 'pysrt'":**
- Install dependencies: `pip install pysrt pandas numpy tqdm`

## Key Takeaway

This example shows that creating FAIR, AI-ready wildlife datasets requires more than just organizing files—it requires thoughtful integration of heterogeneous data sources, adherence to community standards, and comprehensive documentation that serves both human researchers and machine learning systems.

## Learn More

- **Dataset on Hugging Face:** https://huggingface.co/datasets/imageomics/kabr-behavior-telemetry
- **Darwin Core Standards:** https://dwc.tdwg.org/
- **WildFAIRx Principles:** See main repository README
- **FAIR Data Principles:** https://www.go-fair.org/fair-principles/


