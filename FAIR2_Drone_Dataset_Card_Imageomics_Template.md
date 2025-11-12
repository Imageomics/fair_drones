---
# FAIR² DRONE DATASET CARD METADATA (YAML Front Matter)
# This section provides machine-readable metadata following Hugging Face standards
# Extended with FAIR² and Darwin Core compliance fields

license: cc-by-4.0  # Change to appropriate license (cc0-1.0, cc-by-4.0, etc.)
language:
- en
pretty_name: "Your Dataset Name Here"

task_categories: 
  - object-detection
  - image-classification
  - video-classification
  # Add others: image-segmentation, object-tracking, keypoint-detection, etc.

tags:
  - biology
  - ecology
  - wildlife-monitoring
  - drone
  - uav
  - aerial-imagery
  # Add specific tags: your species, habitat type, location, etc.

size_categories: 
  - 10K<n<100K  # Update based on your dataset size

# FAIR² COMPLIANCE METADATA
fair2_compliance:
  findable:
    doi: ""  # Add DOI once generated
    metadata_registry: ["DataCite", "GBIF"]  # Where metadata will be deposited
  accessible:
    open_access: true
    authentication_required: false
  interoperable:
    standards: ["Darwin Core", "TDWG", "FAIR2"]
  reusable:
    license_clear: true
    provenance_documented: true
  ai_ready:
    machine_readable: true
    structured_annotations: true

# DARWIN CORE COMPLIANCE (following TDWG standards)
darwin_core:
  event_coverage:
    start_date: "YYYY-MM-DD"
    end_date: "YYYY-MM-DD"
    decimal_latitude: 0.0  # Representative center point
    decimal_longitude: 0.0
    coordinate_uncertainty_meters: 0
    locality: "Location name"
    habitat: "Habitat description"
  
  occurrence_info:
    kingdom: "Animalia"
    taxa_included: []  # List of scientific names
    sampling_protocol: "Brief description of survey method"

# PLATFORM SPECIFICATIONS
platform:
  type: "UAV"  # UAV, AUV, ROV, USV, UGV
  manufacturer: ""
  model: ""
  autonomy_mode: ""  # manual, semi-autonomous, fully-autonomous
  
# SENSOR SPECIFICATIONS  
sensors:
  - type: "RGB"  # RGB, thermal, multispectral, LiDAR
    manufacturer: ""
    model: ""
    resolution: []  # [width, height] in pixels
    
# MISSION PARAMETERS
mission:
  altitude_m: 0  # Typical operating altitude AGL
  speed_ms: 0  # Typical flight speed
  telemetry_available: false

---

<!-- 
=============================================================================
FAIR² DRONE DATASET CARD - EXTENDED IMAGEOMICS TEMPLATE
=============================================================================

This dataset card implements the FAIR² Drone Data Standard for wildlife monitoring.
It extends the standard Imageomics template with additional sections for:
- Darwin Core biodiversity metadata
- Platform and sensor specifications  
- Mission-level operational metadata
- Cross-disciplinary annotation formats

Fields marked with ⚠️ are REQUIRED for FAIR² compliance
Fields marked with 🌿 are REQUIRED for Darwin Core compliance
Fields marked with 🤖 are REQUIRED for AI-readiness

For more information on the FAIR² Drone Data Standard, see: [paper link]
-->

<!-- Include representative image of your dataset -->
|![Example Image](https://huggingface.co/datasets/your-org/your-dataset/resolve/main/examples/example_001.jpg)|
|:--|
|**Figure 1.** Representative image from the dataset showing [describe what's shown].|

# Dataset Card for [Dataset Name]

<!-- 
Quick summary: What is this dataset and what can it be used for?
Example: "Multi-species aerial wildlife dataset from East African savannas, 
supporting detection, tracking, and behavioral classification tasks."
-->

**Quick Summary:** [One-sentence description]

## Dataset Details

### Dataset Description

⚠️ **Essential Information:**
- **Curated by:** [List all data collectors and annotators]
- **Funded by:** [Funding sources]
- **Language(s):** English (metadata and documentation)
- **License:** [License name with link]
- **Homepage:** [Dataset website URL]
- **Repository:** [Code/tools repository]
- **Paper:** [Link to paper describing dataset]
- **DOI:** [Persistent identifier]

**Full Description:**

[2-3 paragraphs describing:
- What: Species/ecosystems studied, data types collected
- Why: Research objectives and conservation applications
- How: Collection methodology at high level
- When: Temporal coverage and sampling frequency
- Where: Geographic locations and habitats]

### Supported Tasks and Applications

This dataset supports the following computer vision and ecological analysis tasks:

**🤖 Computer Vision Tasks:**
- [ ] Object Detection (bounding boxes around animals)
- [ ] Instance Segmentation (pixel-level masks)
- [ ] Multi-Object Tracking (ID consistency across frames)
- [ ] Re-identification (individual recognition)
- [ ] Keypoint Detection (pose estimation)
- [ ] Behavior Recognition (activity classification)
- [ ] Other: [specify]

**🌿 Ecological Applications:**
- [ ] Population abundance estimation
- [ ] Behavioral analysis
- [ ] Habitat use patterns
- [ ] Species distribution modeling
- [ ] Conservation monitoring
- [ ] Other: [specify]

**🤖 Robotics Applications:**
- [ ] Navigation algorithm testing
- [ ] Perception system benchmarking
- [ ] Autonomy evaluation
- [ ] Multi-platform coordination
- [ ] Other: [specify]

**Benchmark Results:**

[If available, provide baseline performance metrics]

| Method | Detection mAP@50 | Tracking MOTA | Behavior Acc | Reference |
|--------|------------------|---------------|--------------|-----------|
| YOLOv8 | 0.XX | - | - | [link] |
| ... | ... | ... | ... | ... |

## Dataset Structure

### Directory Organization

```
dataset/
├── images/
│   ├── train/
│   │   ├── rgb/
│   │   │   └── {mission_id}_{frame_id}.jpg
│   │   └── thermal/  # if applicable
│   ├── val/
│   └── test/
├── annotations/
│   ├── train/
│   │   ├── coco_format.json
│   │   ├── yolo_format/
│   │   └── tracking/  # if applicable
│   ├── val/
│   └── test/
├── telemetry/  # if available
│   └── {mission_id}_telemetry.csv
├── metadata/
│   ├── darwin_core_events.csv  # 🌿 Darwin Core Event records
│   ├── darwin_core_occurrences.csv  # 🌿 Darwin Core Occurrence records
│   ├── missions.csv  # Mission-level metadata
│   ├── sensors.json  # Sensor specifications
│   └── species_info.json  # Taxonomic information
└── README.md
```

### Data Instances

**Images:**
- Format: [JPG, PNG, TIFF, etc.]
- Resolution: [width] x [height] pixels
- Bit depth: [8-bit, 16-bit, etc.]
- Color space: [RGB, grayscale, thermal, etc.]
- File size range: [X-Y MB]

**Naming Convention:**
```
{mission_id}_{frame_number}[_{sensor_type}].{extension}
Example: AWS2024-045_003821.jpg
         └─mission─┘ └frame─┘

Mission ID: Unique identifier for each flight (format: [prefix]-[number])
Frame Number: Sequential frame number within mission (zero-padded to 6 digits)
Sensor Type: Optional suffix for multi-sensor data (_rgb, _thermal, etc.)
```

**Temporal Information:**
- Date range: [YYYY-MM-DD to YYYY-MM-DD]
- Time of day: [dawn, morning, midday, afternoon, dusk, night]
- Seasons covered: [list seasons]
- Frame timestamps: [included in telemetry files / EXIF data / separate CSV]

### Data Fields

#### 🌿 Darwin Core Event Metadata (`metadata/darwin_core_events.csv`)

⚠️ Required fields for Darwin Core compliance:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `eventID` | string | Unique identifier for sampling event | "AWS2024-045" |
| `eventDate` | date | Date of survey (ISO 8601) | "2024-03-15" |
| `eventTime` | time | Time of survey start | "06:30:00+03:00" |
| `decimalLatitude` | float | Latitude in decimal degrees (WGS84) | -2.3456 |
| `decimalLongitude` | float | Longitude in decimal degrees (WGS84) | 34.8123 |
| `coordinateUncertaintyInMeters` | integer | GPS precision | 5 |
| `geodeticDatum` | string | Coordinate system | "WGS84" |
| `locality` | string | Named location | "Serengeti National Park, Sector A3" |
| `habitat` | string | Habitat type | "Open savanna with scattered Acacia" |
| `samplingProtocol` | string | Survey method | "UAV transect at 60m AGL, 5m/s" |
| `sampleSizeValue` | float | Area/duration surveyed | 250 |
| `sampleSizeUnit` | string | Unit for sample size | "hectares" |
| `samplingEffort` | string | Effort description | "45 min flight, 70% overlap" |

Optional but recommended:
- `minimumElevationInMeters`: Ground elevation at site
- `weather`: Weather conditions during survey
- `fieldNotes`: Additional observations

#### 🌿 Darwin Core Occurrence Metadata (`metadata/darwin_core_occurrences.csv`)

⚠️ Required fields for Darwin Core compliance:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `occurrenceID` | string | Unique observation identifier | "AWS2024-045_003821_001" |
| `eventID` | string | Links to Event record | "AWS2024-045" |
| `scientificName` | string | Full scientific name | "Loxodonta africana (Blumenbach, 1797)" |
| `kingdom` | string | Taxonomic kingdom | "Animalia" |
| `phylum` | string | Taxonomic phylum | "Chordata" |
| `class` | string | Taxonomic class | "Mammalia" |
| `order` | string | Taxonomic order | "Proboscidea" |
| `family` | string | Taxonomic family | "Elephantidae" |
| `genus` | string | Taxonomic genus | "Loxodonta" |
| `species` | string | Specific epithet | "africana" |
| `taxonRank` | string | Rank of identification | "species" |
| `individualCount` | integer | Number of individuals | 12 |

Optional but recommended:
- `lifeStage`: "adult", "juvenile", "calf"
- `sex`: "male", "female", "undetermined"
- `behavior`: Behavioral state during observation
- `occurrenceRemarks`: Additional notes

#### 🤖 Computer Vision Annotations

**COCO Format** (`annotations/train/coco_format.json`):
```json
{
  "info": {
    "description": "[Dataset name and description]",
    "version": "1.0",
    "year": 2024,
    "date_created": "2024-01-15"
  },
  "licenses": [...],
  "images": [
    {
      "id": 1,
      "file_name": "AWS2024-045_003821.jpg",
      "width": 5280,
      "height": 2970,
      "date_captured": "2024-03-15T06:35:42+03:00",
      "mission_id": "AWS2024-045",
      "altitude_m": 60,
      "gsd_cm_per_px": 1.5
    }
  ],
  "annotations": [
    {
      "id": 1,
      "image_id": 1,
      "category_id": 1,
      "bbox": [x, y, width, height],
      "area": 12543.5,
      "iscrowd": 0,
      "attributes": {
        "occlusion": "none",
        "truncation": false,
        "life_stage": "adult",
        "behavior": "foraging",
        "group_size": 12,
        "confidence": 0.95
      },
      "occurrence_id": "AWS2024-045_003821_001"  # Links to Darwin Core
    }
  ],
  "categories": [
    {
      "id": 1,
      "name": "african_elephant",
      "supercategory": "mammal",
      "scientific_name": "Loxodonta africana"
    }
  ]
}
```

**Tracking Format** (if applicable):

MOT Challenge format with species labels:
```
{frame_number},{object_id},{bbox_left},{bbox_top},{bbox_width},{bbox_height},{confidence},{species_id},{life_stage},{behavior}
```

### Data Splits

| Split | Images | Annotations | Species Coverage | Temporal Coverage |
|-------|--------|-------------|------------------|-------------------|
| Train | X,XXX | XX,XXX | All species | All seasons |
| Validation | X,XXX | XX,XXX | All species | Stratified |
| Test | X,XXX | XX,XXX | All species | Held-out missions |

**Split Methodology:**

[Describe how splits were created, e.g.:]
- Spatially stratified: Each split contains data from all survey locations
- Temporally balanced: Seasonal representation maintained across splits
- Mission-based: Complete missions assigned to splits (no frame-level splitting)
- Class-balanced: Similar species distributions across splits

## Platform and Mission Specifications

### 🚁 Platform Details

**Type:** [UAV / AUV / ROV / USV / UGV]

**Hardware:**
- Manufacturer: [e.g., DJI, senseFly, custom]
- Model: [e.g., Matrice 300 RTK]
- Weight: [X.X kg]
- Max flight time: [XX min]
- Max speed: [XX m/s]
- Wind resistance: [XX m/s]

**Autonomy:**
- Mode: [manual / semi-autonomous / fully-autonomous]
- Navigation: [waypoint / grid / adaptive / orbit]
- Collision avoidance: [Yes/No]
- Return-to-home: [Yes/No]

**Payload:**
- Max payload: [X.X kg]
- Gimbal: [Yes/No, X-axis stabilization]

### 📷 Sensor Specifications

**Primary Sensor: [Name]**
- Type: [RGB / thermal / multispectral / hyperspectral / LiDAR]
- Manufacturer: [e.g., DJI, FLIR, MicaSense]
- Model: [e.g., Zenmuse H20T]
- Resolution: [XXXX x XXXX pixels]
- Sensor size: [XX.X x XX.X mm]
- Focal length: [XX mm]
- Field of view: [XX° x XX° (H x V)]
- Frame rate: [X fps]
- Bit depth: [X-bit]

**Spectral Bands** (if applicable):
| Band | Wavelength (nm) | Purpose |
|------|-----------------|---------|
| Red | 590-700 | Vegetation health |
| ... | ... | ... |

**Calibration:**
- Calibrated: [Yes/No]
- Method: [e.g., checkerboard, Agisoft Lens]
- Date: [YYYY-MM-DD]
- Files included: [Yes/No, location if yes]

**Synchronization** (for multi-sensor):
- Method: [GPS time / hardware trigger / software sync]
- Accuracy: [±X ms]

### 🗺️ Mission Parameters

**Flight Specifications:**
- Altitude: [XX-XX m AGL (above ground level)]
- Speed: [X-X m/s]
- Flight pattern: [grid / transect / orbit / adaptive]
- Coverage per mission: [XXX hectares]
- Image overlap: [XX% forward, XX% side]
- Ground sampling distance: [X.X cm/pixel]

**Telemetry Data:**
- Available: [Yes/No]
- Format: [CSV / GPX / KML / ROS bag]
- Sampling rate: [XX Hz]
- Fields included:
  - [ ] GPS (lat/lon/alt)
  - [ ] IMU (roll/pitch/yaw)
  - [ ] Speed (ground/vertical)
  - [ ] Battery level
  - [ ] Gimbal angles
  - [ ] [Other]

**Environmental Conditions:**
- Temperature range: [XX-XX°C]
- Wind speed range: [X-XX m/s]
- Weather: [clear / partly cloudy / overcast]
- Time of day: [dawn / morning / afternoon / dusk]
- Season: [dry season / wet season / transitional]

### 🔍 Sampling Protocol

⚠️ Full sampling protocol description:

[Detailed description following Barnas et al. (2020) reporting standards:]

1. **Survey Design:**
   - [Systematic grid / transects / random sampling / adaptive]
   - [Spacing, coverage strategy]
   
2. **Flight Operations:**
   - [Pre-flight checks and procedures]
   - [Operator training and certification]
   - [Safety protocols]
   
3. **Data Collection:**
   - [Trigger method: time-based, distance-based, manual]
   - [Collection parameters]
   
4. **Quality Control:**
   - [In-field QC procedures]
   - [Data backup and verification]

### 📋 Permits and Compliance

**Permits Obtained:**
- [Civil Aviation Authority permit number and type]
- [Research/collection permits]
- [Land access permissions]

**Regulations Followed:**
- [National/regional UAV regulations]
- [IUCN Best Practice Guidelines]
- [Institutional animal research guidelines]

**Ethics Approval:**
- [IRB/IACUC approval number]
- [Ethics committee name]

**Animal Welfare Protocol:**
- [Minimum altitude maintained]
- [Behavioral disturbance monitoring]
- [Flight restrictions near sensitive areas]

## Dataset Creation

### Curation Rationale

[Describe the motivation for creating this dataset:]
- Scientific questions driving data collection
- Gap in existing datasets this fills
- Why this location/species/approach was chosen
- Intended use cases

### Source Data

#### Data Collection and Processing

**Field Collection** (describe what YOU did):

1. **Planning:**
   - [Site selection criteria]
   - [Temporal sampling design]
   
2. **Collection:**
   - [Flight execution]
   - [Data storage and backup in field]
   
3. **Post-Processing:**
   - [Image processing pipeline]
   - [Quality filtering criteria]
   - [Georeferencing method]
   - [Radiometric correction (if applicable)]

**Software and Tools Used:**
- Flight planning: [software name and version]
- Image processing: [e.g., Agisoft Metashape, Pix4D]
- Georeferencing: [e.g., QGIS, ArcGIS]
- Annotation: [e.g., CVAT, Label Studio]

#### Who are the source data producers?

**Field Team:**
- [Names and roles of data collectors]
- [Affiliations]
- [Relevant expertise]

**Local Collaboration:**
- [Local partners and communities involved]
- [Traditional knowledge incorporation]
- [Benefit sharing arrangements]

### Annotations

#### Annotation Process

**🤖 Annotation Method:**
- [ ] Fully manual
- [ ] Semi-automated (pre-labeling + review)
- [ ] Fully automated (with human validation)

**Tools Used:**
- Software: [e.g., CVAT, Label Studio, VGG Image Annotator]
- Version: [X.X.X]

**Annotation Guidelines:**
- [Link to annotation guidelines document]
- Key rules:
  - [e.g., "Mark all visible individuals, even if partially occluded"]
  - [e.g., "Bounding box includes entire body when visible"]
  - [e.g., "Behavioral state recorded at moment of frame capture"]

**Quality Control:**
- Annotator training: [X hours training on example data]
- Inter-annotator agreement: [Metric used and value, e.g., Cohen's kappa = 0.89]
- Review process: [e.g., "Senior ecologist reviewed 100% of annotations"]
- Difficult cases: [How edge cases were handled]
- Annotation confidence: [Whether confidence scores are included]

**Annotation Coverage:**
- Fully annotated: [Yes/No]
- If partial: [e.g., "Every 10th frame", "Keyframes only", "Objects >50px only"]
- Missing annotations: [Description of any gaps]

#### Who are the annotators?

**Annotator Team:**
- Number of annotators: [X]
- Expertise: [e.g., "Graduate students in ecology with 2+ years wildlife identification experience"]
- Training provided: [Description]
- Compensation: [Academic credit / paid / volunteer]

**Subject Matter Experts:**
- [Names and credentials of validators]
- [Role in annotation process]

### Personal and Sensitive Information

⚠️ **Privacy and Security Considerations:**

**Human Subjects:**
- [ ] No humans visible in imagery
- [ ] Humans may be incidentally captured but not identifiable
- [ ] Humans visible; IRB approval obtained (#[number])
- [ ] Imagery collected over private property with permission

**Endangered Species:**
- [ ] No endangered species
- [ ] Contains endangered/threatened species: [list species]
- [ ] Location precision reduced to [X km] to protect sensitive species
- [ ] Consultation with conservation authorities: [details]

**Cultural Sensitivity:**
- [ ] No cultural concerns identified
- [ ] Traditional lands: [Consultation and approval process]
- [ ] Sacred sites: [Areas excluded from dataset]

**Security:**
- [ ] No security concerns
- [ ] Exact coordinates obscured for: [reason]
- [ ] Data access restricted: [describe restrictions]

## Considerations for Using the Data

### Dataset Statistics

**Species Distribution:**

| Species (Scientific Name) | Common Name | Train | Val | Test | Total |
|---------------------------|-------------|-------|-----|------|-------|
| *Species name* | Common name | XXX | XX | XX | XXX |
| ... | ... | ... | ... | ... | ... |

**Class Balance:**
- Balanced: [Yes/No]
- Imbalance ratio: [Most common : least common = XX:1]
- Long-tailed distribution: [Yes/No]

**Image Characteristics:**
- Resolution range: [XXX x XXX to XXXX x XXXX]
- Lighting conditions: [bright: XX%, overcast: XX%, low-light: XX%]
- Occlusion levels: [none: XX%, partial: XX%, heavy: XX%]
- Crowd density: [sparse: XX%, moderate: XX%, dense: XX%]
- Scale variation: [Describe object size range]

**Detection Difficulty Metadata:**

| Difficulty Factor | Easy (%) | Medium (%) | Hard (%) |
|-------------------|----------|------------|----------|
| Occlusion | XX | XX | XX |
| Crowd density | XX | XX | XX |
| Scale (small objects) | XX | XX | XX |
| Weather/lighting | XX | XX | XX |

### Bias, Risks, and Limitations

**⚠️ Known Biases:**

1. **Geographic Bias:**
   - [e.g., "Data collected only from protected areas, may not represent human-modified landscapes"]
   
2. **Temporal Bias:**
   - [e.g., "Morning flights only, nocturnal behavior not captured"]
   
3. **Species Bias:**
   - [e.g., "Large-bodied species over-represented due to detection ease"]
   
4. **Environmental Bias:**
   - [e.g., "Dry season only, no data on wet season habitat use"]

5. **Detection Bias:**
   - [e.g., "Detection probability varies by habitat cover"]
   - [e.g., "Small animals (<50cm) under-detected at this altitude"]

**Technical Limitations:**

- **Image Quality:** [Describe any systematic quality issues]
- **Coverage Gaps:** [Areas/times not sampled]
- **Annotation Limitations:** [e.g., "Cannot determine sex for most species"]
- **Calibration:** [If sensors not fully calibrated]

**Ethical Limitations:**

- **Animal Welfare:** [Potential disturbance noted]
- **Data Usage:** [e.g., "Coordinates should not be used for poaching"]
- **Community Concerns:** [Any expressed concerns]

### Recommendations

**Best Practices for Using This Dataset:**

1. **For Detection/Tracking Models:**
   - [e.g., "Account for altitude-dependent scale variation"]
   - [e.g., "Consider species-specific detection thresholds"]

2. **For Ecological Analysis:**
   - [e.g., "Apply detection probability corrections for sparse vegetation"]
   - [e.g., "Do not generalize beyond dry season without additional data"]

3. **For Transfer Learning:**
   - [e.g., "Model trained at 60m may require fine-tuning for other altitudes"]
   - [e.g., "RGB-thermal fusion recommended for dense vegetation"]

4. **Ethical Use:**
   - [e.g., "Do not share precise coordinates publicly"]
   - [e.g., "Consider conservation implications of automated detection tools"]

**What This Dataset Should NOT Be Used For:**

- [e.g., "Estimating population density without accounting for detection probability"]
- [e.g., "Training models for use in unethical wildlife targeting"]
- [e.g., "Generalizing to wet season behavior without caveat"]

## Multimodal Linkages

**Associated Datasets** (if applicable):

- **Camera Trap Data:** [Link and description of linkage]
- **GPS Collar Data:** [Link and description]
- **Acoustic Data:** [Link and description]
- **Environmental Sensors:** [Link and description]

**Synchronization:**
- Temporal alignment: [How data streams are synchronized]
- Spatial alignment: [Coordinate system transformation details]

## Licensing Information

**Dataset License:** [Full license name]

This dataset is released under [license name]. This means you are free to:
- ✓ Share — copy and redistribute the material
- ✓ Adapt — remix, transform, and build upon the material
- [Other permissions]

Under the following terms:
- [License conditions, e.g., Attribution, NonCommercial, ShareAlike]

**Citation Requirement:** If you use this dataset, you MUST cite both the dataset and associated paper (see Citation section).

**Image Licensing:** [If different from compilation]
- Individual images may have different licenses: [describe]
- See `metadata/licenses.csv` for per-image license information

**Code License:** [If releasing code alongside data]
- Analysis scripts and tools: [license, e.g., MIT]

## Citation

⚠️ **If you use this dataset, please cite:**

**Dataset:**
```bibtex
@misc{yourdataset2024,
  author = {Last, First and Last, First},
  title = {Dataset Title},
  year = {2024},
  publisher = {Hugging Face},
  url = {https://huggingface.co/datasets/your-org/your-dataset},
  doi = {10.XXXX/XXXXX}
}
```

**Paper:**
```bibtex
@article{yourpaper2024,
  title = {Paper Title},
  author = {Last, First and Last, First},
  journal = {Journal Name},
  year = {2024},
  volume = {X},
  pages = {XX-XX},
  doi = {10.XXXX/XXXXX}
}
```

**FAIR² Drone Data Standard:**
```bibtex
@article{kline2025fair2,
  title = {Toward a FAIR² Standard for Drone-Based Wildlife Monitoring Datasets},
  author = {Kline, Jenna and others},
  year = {2025},
  doi = {10.XXXX/XXXXX}
}
```

## Acknowledgements

This work was supported by [funding source]. 

We thank:
- [Field assistance]
- [Local communities and authorities]
- [Annotation team]
- [Technical support]

This work was supported by the [Imageomics Institute](https://imageomics.org), which is funded by the US National Science Foundation's Harnessing the Data Revolution (HDR) program under [Award #2118240](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2118240).

**Conservation Partners:**
- [Park/reserve management]
- [Conservation organizations]
- [Local communities]

**Data Collection Permits:** [List major permits with gratitude to issuing authorities]

## Validation and Quality Metrics

**🤖 AI-Readiness Validation:**

- [ ] Machine-readable metadata (YAML front matter complete)
- [ ] Structured annotations in standard format
- [ ] Train/val/test splits clearly defined
- [ ] Class distribution documented
- [ ] Data loading code provided
- [ ] Example notebooks provided

**🌿 Darwin Core Validation:**

- [ ] Event records complete and valid
- [ ] Occurrence records complete and valid
- [ ] Scientific names validated against taxonomic backbone
- [ ] Coordinates in WGS84
- [ ] Sampling protocol documented
- [ ] Links to GBIF established (if applicable)

**⚠️ FAIR² Compliance Checklist:**

- [ ] **Findable:** DOI assigned, metadata in registries
- [ ] **Accessible:** Open access, clear download instructions
- [ ] **Interoperable:** Standard formats, vocabulary standards followed
- [ ] **Reusable:** Clear license, provenance documented, quality metrics reported
- [ ] **AI-Ready:** Machine-readable, structured, versioned

## Code and Tools

**Data Loading:**

```python
# Example: Load dataset using Hugging Face datasets library
from datasets import load_dataset

dataset = load_dataset("your-org/your-dataset")

# Access images and annotations
train_data = dataset['train']
for sample in train_data:
    image = sample['image']
    annotations = sample['annotations']
    # Your code here
```

**Visualization Tools:**
- [Link to visualization scripts]
- [Link to example notebooks]

**Evaluation Scripts:**
- [Link to evaluation code for benchmarking]

## Glossary

**AGL:** Above Ground Level - altitude measured from terrain surface below
**Darwin Core:** Biodiversity data standard maintained by TDWG
**FAIR²:** Extension of FAIR principles for AI-ready datasets
**GSD:** Ground Sampling Distance - real-world size represented by one pixel
**UAV:** Unmanned Aerial Vehicle (drone)
**TDWG:** Biodiversity Information Standards organization

## Dataset Card Authors

[List names of card authors]

## Dataset Card Contact

For questions about this dataset:
- Email: [contact email]
- Issues: [link to issue tracker]
- Discussions: [link to discussion board]

---

**Version History:**

- v1.0.0 (YYYY-MM-DD): Initial release
- [Future versions as dataset is updated]

---

*This dataset card follows the FAIR² Drone Data Standard (Kline et al., 2025) and extends the Imageomics dataset card template.*
