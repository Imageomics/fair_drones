# KABR Behavior Telemetry Data Dictionary

This document provides detailed descriptions of all data files and their fields in the KABR Behavior Telemetry dataset.

## Dataset Files

### Core Data Files

#### `data/occurrences/`
Frame-by-frame occurrence records for each video, combining detection tracks, behavior annotations, and telemetry data.

**Files:** One CSV per video, named `{date}-{video_id}.csv` (e.g., `11_01_23-DJI_0977.csv`)

**Key Fields:**
- `date`: Recording date in DD_MM_YY format
- `video_id`: DJI video identifier (e.g., DJI_0977)
- `frame`: Frame number in the video sequence (0-indexed)
- `date_time`: Timestamp in format "YYYY-MM-DD HH:MM:SS,milliseconds,microseconds"
- `id`: Mini-scene identifier (track ID for behavioral sequences)
- `latitude`: GPS latitude in decimal degrees (WGS84)
- `longitude`: GPS longitude in decimal degrees (WGS84)
- `altitude`: Altitude in meters above sea level
- `iso`: Camera ISO setting
- `shutter`: Shutter speed value
- `fnum`: Aperture f-number
- `ev`: Exposure value
- `ct`: Color temperature
- `color_md`: Color mode descriptor
- `focal_len`: Lens focal length in millimeters
- `dzoom_ratio`: Digital zoom ratio
- `xtl`, `ytl`, `xbr`, `ybr`: Bounding box coordinates (top-left and bottom-right)
- `z_order_x`, `z_order_y`: Display depth ordering for overlapping annotations
- `label`: Object class label (e.g., "zebra", "giraffe")
- `source`: Annotation source
- `keyframe_x`, `keyframe_y`: Whether frame is a tracking keyframe
- `outside_x`, `outside_y`: Whether object is outside frame bounds
- `occluded_x`, `occluded_y`: Whether object is occluded
- `points`: Polygon points for behavioral sequences
- `behaviour`: Behavioral classification (e.g., "walking", "grazing", "running")

**Record Count:** Varies by video; typically 10,000-66,000 frames per video
**Coverage:** 47 videos with complete data
**Missing Values:** Frames without detections/annotations have null values for annotation fields

---

#### `data/video_events.csv`
Darwin Core Event records for individual video recordings.

**Record Count:** 68 videos (47 with occurrence data)

**Fields:**

**Identifiers:**
- `eventID`: Unique event identifier (format: "KABR-2023:{session}:{video_id}")
- `parentEventID`: Links to session_events (format: "KABR-2023:{session}")

**Event Classification:**
- `eventType`: Type of sampling event ("video recording")
- `eventDate`: Recording date (ISO 8601: YYYY-MM-DD)
- `eventTime`: Video start time (HH:MM:SS)
- `endTime`: Video end time (HH:MM:SS)

**Geographic Information:**
- `decimalLatitude`: Launch point latitude in decimal degrees (WGS84)
- `decimalLongitude`: Launch point longitude in decimal degrees (WGS84)
- `geodeticDatum`: Coordinate reference system ("WGS84")
- `minimumElevationInMeters`: Minimum altitude during video
- `maximumElevationInMeters`: Maximum altitude during video
- `footprintWKT`: Geographic bounding box in Well-Known Text format

**Sampling Protocol:**
- `samplingProtocol`: "Continuous aerial video recording"

**Associated Resources:**
- `associatedMedia`: JSON object with paths to detection and behavior annotation files
  ```json
  {
    "detection": "path/to/DJI_XXXX_tracks.xml",
    "behavior": ["path/to/trackID.xml", ...]
  }
  ```

**Remarks:**
- `eventRemarks`: Description of video file (e.g., "Video file DJI_0977.MP4")

---

#### `data/session_events.csv`
Darwin Core Event records for field sessions (missions/flights).

**Record Count:** 17 sessions (14 with occurrence data)

**Fields:**

**Identifiers and Classification:**
- `eventID`: Unique session identifier (format: "KABR-2023:{date}_{session}")
- `parentEventID`: Dataset identifier ("KABR-2023")
- `eventType`: Type of event ("drone survey")

**Temporal Coverage:**
- `eventDate`: Session date (ISO 8601: YYYY-MM-DD)
- `eventTime`: Session start time (HH:MM:SS)
- `endTime`: Session end time (HH:MM:SS)
- `year`, `month`, `day`: Parsed date components

**Geographic Coverage:**
- `launchLatitude`: Drone launch point latitude (from first video)
- `launchLongitude`: Drone launch point longitude (from first video)
- `decimalLatitude`: Latitude range across session "[min, max]"
- `decimalLongitude`: Longitude range across session "[min, max]"
- `geodeticDatum`: "WGS84"
- `coordinateUncertaintyInMeters`: GPS precision
- `minimumElevationInMeters`: Minimum altitude across all videos
- `maximumElevationInMeters`: Maximum altitude across all videos
- `footprintWKT`: Session bounding box in WKT format
- `locationID`: "MPALA-KENYA"
- `locality`: "Mpala Research Centre"
- `country`: "Kenya"
- `countryCode`: "KE"

**Habitat and Environment:**
- `habitat`: Habitat type description (e.g., "Open grassy habitat with some scattered bushes")

**Sampling Details:**
- `samplingProtocol`: Detailed protocol description
- `sampleSizeValue`: Empty (intended for area surveyed)
- `sampleSizeUnit`: "minutes"
- `samplingEffort`: Number and description of video segments

**Taxonomic Information:**
- `organismQuantity`: Number of individual animals observed
- `organismQuantityType`: "herd size"

**Observations:**
- `eventRemarks`: Field notes and observations
- `_species_common`: Common name(s) of observed species
- `_species_commonNames`: Additional common names
- `_n_individuals`: Number of individuals
- `_n_videos`: Number of videos in session

**Associated Data:**
- `associatedMedia`: JSON object listing videos, focal follows, and scan samples
  ```json
  {
    "video": ["DJI_0977", "DJI_0978", ...],
    "focal": [],
    "scan": []
  }
  ```
- `associatedReferences`: Airdata telemetry file names
- `_telemetry_file_raw`: Raw telemetry file status notes

**Ecological Extensions (Humboldt Eco):**
- `eco:inventoryTypes`: "restrictedSearch"
- `eco:protocolNames`: "KABR Drone Video Survey Protocol"
- `eco:protocolDescriptions`: Protocol description
- `eco:protocolReferences`: "https://doi.org/10.48550/arXiv.2510.02030"
- `eco:isAbundanceReported`: True
- `eco:isAbundanceCapReported`: False
- `eco:abundanceUnit`: "individuals"
- `eco:isVegetationCoverReported`: True/False
- `eco:vegetationCoverUnit`: "Bitterlich score (0-10 scale)" (when applicable)
- `eco:isTaxonCompletenessReported`: True
- `eco:taxonCompletenessProtocols`: "All visible target taxa annotated in video frames with bounding boxes"
- `eco:isAbsenceReported`: False
- `eco:hasNonTargetTaxa`: Empty
- `eco:nonTargetTaxa`: Empty
- `eco:targetTaxonomicScope`: Scientific names of target species
- `eco:excludedTaxonomicScope`: Empty
- `eco:samplingPerformedBy`: Empty
- `eco:siteCount`: 1
- `eco:siteNestingDescription`: "Single focal group follow per session"
- `eco:verbatimSiteDescriptions`: Empty

**Quality Flags:**
- `_needs_verification`: Data quality flag

---

### Scripts

#### `scripts/merge_behavior_telemetry.py`
Merges SRT metadata, detection tracks, and behavior annotations into occurrence files.

**Usage:**
```bash
python scripts/merge_behavior_telemetry.py \
  --data_path /path/to/video/directories \
  --outpath /path/to/output/ \
  [--skip-airdata]
```

**Arguments:**
- `--data_path`: Directory containing video folders (format: DATE-VIDEO_ID)
- `--session_data_path`: Path to SRT files (default: preset path)
- `--flight_logs_path`: Path to decrypted flight logs (default: preset path)
- `--skip-airdata`: Skip merging with flight log data
- `--write`: Whether to write output (default: True)
- `--outpath`: Output directory for CSV files

**Input Requirements:**
- Video directories with structure:
  - `metadata/{video_id}_tracks.xml`: Detection bounding boxes
  - `actions/*.xml`: Behavior annotation files
- SRT files with GPS and camera metadata
- (Optional) Flight log CSV files with telemetry

**Output:**
- One CSV per video in occurrence format

---

#### `scripts/update_video_events.py`
Updates video_events.csv with associatedMedia paths to detection and behavior files.

**Usage:**
```bash
python scripts/update_video_events.py \
  --video_events data/video_events.csv \
  --data_path /path/to/video/directories \
  [--output output_path.csv]
```

**What it does:**
- Scans video directories for detection and behavior annotation files
- Creates relative paths from kabr-behavior-telemetry/data to annotation files
- Updates associatedMedia field with JSON structure

---

#### `scripts/add_event_times.py`
Extracts start and end times from occurrence files and adds to video_events.csv.

**Usage:**
```bash
python scripts/add_event_times.py \
  --video_events data/video_events.csv \
  --occurrences data/occurrences/ \
  [--output output_path.csv]
```

**What it does:**
- Reads date_time from first and last rows of each occurrence file
- Extracts time component (HH:MM:SS)
- Updates eventTime and endTime fields

---

#### `scripts/add_gps_data.py`
Extracts GPS statistics from occurrence files and adds to event files.

**Usage:**
```bash
python scripts/add_gps_data.py \
  --video_events data/video_events.csv \
  --session_events data/session_events.csv \
  --occurrences data/occurrences/ \
  [--output_video output_video.csv] \
  [--output_session output_session.csv]
```

**What it does:**

For **video_events.csv**:
- Extracts launch point (first GPS coordinate)
- Calculates min/max lat/lon bounds
- Determines altitude range
- Creates WKT footprint

For **session_events.csv**:
- Uses first video's launch point as session launch
- Aggregates bounds across all videos in session
- Formats lat/lon as "[min, max]" ranges
- Creates session-level WKT footprint

---

## Data Relationships

### Hierarchical Structure
```
KABR-2023 (Dataset)
├── KABR-2023:11_01_23_session_1 (Session)
│   ├── KABR-2023:11_01_23_session_1:DJI_0488 (Video Event)
│   │   └── occurrences/11_01_23-DJI_0488.csv (Frame records)
│   └── ...
├── KABR-2023:11_01_23_session_2 (Session)
│   ├── KABR-2023:11_01_23_session_2:DJI_0977 (Video Event)
│   │   └── occurrences/11_01_23-DJI_0977.csv (Frame records)
│   └── ...
...
```

### Linkages
- **session_events** ← linked by parentEventID ← **video_events**
- **video_events** ← associatedMedia paths ← **annotation files**
- **video_events** → referenced by occurrence files → **occurrences/**

---

## Data Processing Pipeline

1. **Field Collection**: Drone flights with video recording
2. **Video Processing**: Frame extraction and annotation
3. **Telemetry Extraction**: SRT files parsed for GPS and camera metadata
4. **Annotation**: Detection boxes and behavior labels added
5. **Merging** (`merge_behavior_telemetry.py`): Combine all data sources
6. **Event Creation**: Generate Darwin Core event records
7. **Metadata Enhancement**:
   - Add associatedMedia paths (`update_video_events.py`)
   - Add temporal bounds (`add_event_times.py`)
   - Add GPS statistics (`add_gps_data.py`)

---

## Darwin Core Compliance

This dataset follows Darwin Core standards (TDWG) with extensions for ecological inventory data (Humboldt Eco).

**Core Classes:**
- **Event**: Recording sessions and individual videos
- **Occurrence**: Frame-level animal detections (in occurrence files)

**Key Standards:**
- Temporal data in ISO 8601 format
- Coordinates in WGS84 decimal degrees
- Controlled vocabularies for taxonomic names
- Unique identifiers for all records

---

## File Formats

### CSV Files
- **Encoding**: UTF-8
- **Delimiter**: Comma (`,`)
- **Quoting**: Double quotes for fields containing delimiters
- **Missing Values**: Empty strings or `NaN`

### JSON Fields
- **Structure**: Valid JSON objects in CSV fields
- **Encoding**: Double-quotes escaped as `""`
- **Arrays**: Square bracket notation `["item1", "item2"]`

### WKT (Well-Known Text)
- **Format**: `POLYGON((lon1 lat1, lon2 lat2, ...))`
- **Coordinate Order**: Longitude first, then latitude
- **Datum**: WGS84 (EPSG:4326)

---

## Quality Assurance

### Known Limitations
- **Missing Occurrence Data**: 21 videos lack occurrence files due to:
  - Missing SRT files
  - Corrupted source data
  - Processing errors
  - Empty annotations

- **GPS Accuracy**: ±5-10 meters typical
- **Timestamp Precision**: Millisecond resolution but may have ±1 second drift

### Data Quality Flags
- `_needs_verification`: Manual review recommended
- `_telemetry_file_raw`: Notes on telemetry file status

---

## Version History

- **v1.1** (2026-01-02): Added GPS data, event times, and occurrence files
- **v1.0** (2024-12-31): Initial release with session and video events

---

## Contact

For questions about this data:
- **Email**: kline.377@osu.edu
- **Issues**: [GitHub repository](https://github.com/Imageomics/kabr-behavior-telemetry)
