# FAIR² Drone Dataset Card: Quick-Start Guide

**For researchers creating or documenting drone-based wildlife datasets**

---

## What You'll Need

**Before starting, gather:**
- [ ] Your image/video files
- [ ] Annotation files (if applicable)
- [ ] Drone/sensor specifications (model numbers)
- [ ] Flight logs or mission notes
- [ ] Research permits and approval numbers
- [ ] Species list with scientific names
- [ ] 2-3 hours of time

---

## Quick Decision Tree: Which Template?

```
START: What's your primary use case?

├─ Object Detection ONLY
│  └─> Use: Detection Template (2 hours to complete)
│      Core + Darwin Core + COCO annotations
│
├─ Multi-Object Tracking
│  └─> Use: Tracking Template (2.5 hours)
│      Detection Template + MOT format + ID protocols
│
├─ Behavior Recognition
│  └─> Use: Behavior Template (3 hours)
│      Detection Template + Ethogram + temporal labels
│
├─ Robotics Benchmarking
│  └─> Use: Platform Template (2.5 hours)
│      Core + Full telemetry + Minimal annotations
│
└─ Multiple Tasks
   └─> Use: Comprehensive Template (3-4 hours)
       All modules activated
```

---

## Three-Tier Approach

### Tier 1: Minimal Compliance (45 minutes - 1 hour)
**Goal:** Dataset is publishable and findable

**Required:**
1. Dataset Overview (10 min)
   - Title, description, license, DOI
2. Basic Darwin Core (15 min)
   - Dates, location, species list
3. Platform basics (10 min)
   - Drone model, sensor type
4. File organization (10 min)
   - Directory structure, formats

**Use case:** Quick dataset release, meets basic FAIR requirements

---

### Tier 2: Recommended Compliance (2-3 hours)
**Goal:** Dataset is cross-domain reusable

**Tier 1 + Add:**
5. Detailed Darwin Core (30 min)
   - Full taxonomic hierarchy, sampling protocol
6. Full platform specs (20 min)
   - Hardware details, autonomy modes
7. Mission parameters (25 min)
   - Flight specs, environmental conditions
8. Annotation specifications (30 min)
   - Format details, quality metrics
9. Dataset statistics (15 min)
   - Class distributions, coverage

**Use case:** Most datasets should aim for this level

---

### Tier 3: Comprehensive (4-6 hours)
**Goal:** Maximum reusability across all domains

**Tier 2 + Add:**
10. Full telemetry data (60 min)
    - GPS logs, IMU data, processing
11. Multimodal linkages (30 min)
    - Connections to other sensor data
12. Detailed validation (45 min)
    - Quality metrics, baseline results
13. Comprehensive limitations (30 min)
    - Bias analysis, ethical considerations

**Use case:** Major dataset releases, benchmark datasets

---

## Step-by-Step Walkthrough (Tier 2)

### Preparation (Before Opening Template)

**5-Minute Prep:**
1. Create a `dataset_info.txt` file with:
   ```
   Dataset name: _______________
   Species studied: _______________
   Location: _______________ (lat/lon if available)
   Dates: _______________ to _______________
   Drone model: _______________
   Camera model: _______________
   Number of images: _______________
   ```

2. Find your:
   - Research permit numbers
   - IRB/IACUC approval number (if applicable)
   - Funding grant numbers
   - Co-author names and affiliations

3. Locate one representative image to calculate:
   - Resolution (check image properties)
   - Ground sampling distance (if known)
   - File size

---

### Phase 1: Core Metadata (30 minutes)

**Module 1: Dataset Overview (10 min)**

Open the template and fill YAML front matter first:

```yaml
license: cc-by-4.0  # Choose appropriate license
pretty_name: "Your Dataset Name"
task_categories: 
  - object-detection  # Add your tasks
tags:
  - wildlife-monitoring
  - [your_species_name]
  - [your_location]
```

Then complete:
- Title and short description *(2 min)*
- Full description (2-3 paragraphs) *(5 min)*
- Authors and contact info *(3 min)*

**Pro tip:** Start with your paper abstract if you have one

---

**Module 2: Data Structure (10 min)**

1. Document your directory tree *(3 min)*
   ```
   dataset/
   ├── images/
   │   ├── train/
   │   ├── val/
   │   └── test/
   └── annotations/
       └── coco_format.json
   ```

2. List file formats *(2 min)*
   - Images: JPG, PNG, etc.
   - Annotations: COCO JSON, YOLO txt, etc.

3. Explain your naming convention *(5 min)*
   - Pattern: `{mission_id}_{frame_id}.jpg`
   - Example: `SERENGETI-2024-045_003821.jpg`

---

**Module 3: Dataset Splits (10 min)**

Fill the table:
| Split | Images | Annotations | How Created |
|-------|--------|-------------|-------------|
| Train | X,XXX | XX,XXX | [e.g., "Missions 1-300"] |
| Val | XXX | X,XXX | [e.g., "Missions 301-350"] |
| Test | XXX | X,XXX | [e.g., "Missions 351-400"] |

Explain your split strategy *(e.g., "stratified by location and season")*

---

### Phase 2: Darwin Core (30 minutes)

**Darwin Core Events (15 min)**

For EACH survey location/date combination, create one Event record:

| Field | Your Data | Where to Find It |
|-------|-----------|------------------|
| eventID | "SERENGETI-2024-045" | Create unique ID per mission |
| eventDate | "2024-03-15" | Flight log or image EXIF |
| eventTime | "06:30:00+03:00" | Flight log |
| decimalLatitude | -2.3456 | Flight log or map |
| decimalLongitude | 34.8123 | Flight log or map |
| coordinateUncertaintyInMeters | 5 | GPS spec sheet (usually 5-10m) |
| locality | "Serengeti NP, Sector A3" | Your study site name |
| habitat | "Open savanna" | Your field notes |
| samplingProtocol | "UAV transect at 60m AGL" | Methods section |
| sampleSizeValue | 250 | Calculated from coverage |
| sampleSizeUnit | "hectares" | Match your calculation |
| samplingEffort | "45 min flight" | Flight log duration |

**Pro tip:** Create a CSV with one row per mission if you have many

---

**Darwin Core Occurrences (15 min)**

1. Get scientific names for your species *(5 min)*
   - Use [GBIF Species](https://www.gbif.org/species/search) to verify
   - Example: "African Elephant" → "Loxodonta africana (Blumenbach, 1797)"

2. Fill taxonomic hierarchy for each species *(10 min)*
   - Copy from GBIF page (they provide all ranks)
   - Create table:

| Species | Kingdom | Phylum | Class | Order | Family | Genus | Species |
|---------|---------|--------|-------|-------|--------|-------|---------|
| African Elephant | Animalia | Chordata | Mammalia | Proboscidea | Elephantidae | Loxodonta | africana |

**Shortcut:** Use the pre-filled template for common species

---

### Phase 3: Platform and Mission (45 minutes)

**Platform Specifications (20 min)**

1. Find your drone specs *(5 min)*
   - Search "[your drone model] specifications" online
   - Or check manufacturer website
   - Record: weight, flight time, max speed, wind resistance

2. Document sensors *(10 min)*
   - Camera: manufacturer, model, resolution
   - Look up: sensor size, focal length, field of view
   - **If you can't find it:** Check EXIF data from images

3. Autonomy details *(5 min)*
   - Manual / waypoint-based / fully autonomous?
   - What features did you use? (orbit, follow, grid)

**Common issue:** "I don't know my gimbal axes"
- Answer: If your camera stays level during flight, it's 3-axis

---

**Mission Parameters (25 min)**

1. Flight specifications *(10 min)*
   ```
   Altitude: 50-80 m AGL
   Speed: 5 m/s
   Pattern: Grid with 70% overlap
   Coverage: 250 hectares per mission
   ```
   
   **How to find:** Flight planning software, image metadata, or estimate from map

2. Environmental conditions *(5 min)*
   - Weather: Clear / Overcast / Partly cloudy
   - Temperature range: From weather station or field notes
   - Wind: From flight log warnings or Beaufort scale estimate

3. Telemetry availability *(5 min)*
   - Do you have flight logs? → Yes
   - What format? → DJI .DAT, CSV, GPX
   - What data? → Check boxes for GPS, IMU, battery, etc.

4. Permits and compliance *(5 min)*
   - List permit numbers
   - Note regulations followed (FAA Part 107, etc.)
   - Animal welfare: "Maintained 50m minimum altitude"

---

### Phase 4: Annotations (45 minutes)

**Annotation Format (15 min)**

1. What task(s) does your dataset support? *(2 min)*
   - [ ] Detection
   - [ ] Tracking
   - [ ] Segmentation
   - [ ] Behavior
   - [ ] Re-ID
   - [ ] Keypoints

2. For each task, specify format *(8 min)*
   - Detection → COCO JSON (describe structure)
   - Tracking → MOT Challenge (describe ID system)
   - Etc.

3. List your label set *(5 min)*
   - Species/classes
   - Behaviors (if applicable)
   - Attributes (age, sex, etc.)

---

**Annotation Quality (15 min)**

1. How were annotations created? *(5 min)*
   - Manual? Semi-automatic? Fully automatic?
   - What tool? (CVAT, Label Studio, etc.)
   - By whom? (student annotators, experts, crowd workers)

2. Quality metrics *(5 min)*
   - How many annotators? 
   - Did you check agreement? (If yes, report metric)
   - Review process? (e.g., "Senior ecologist reviewed all")

3. Confidence scores? *(2 min)*
   - Are they included in your annotation files?

4. Known issues *(3 min)*
   - Any annotation gaps?
   - Difficult cases?
   - Systematic biases?

---

**Annotation Coverage (15 min)**

1. Calculate statistics *(10 min)*
   - Total images
   - Total annotations (count bounding boxes/instances)
   - Annotations per image (min, max, average)
   - Per-class counts

   **Python snippet:**
   ```python
   # For COCO format
   import json
   with open('annotations.json') as f:
       data = json.load(f)
   
   print(f"Images: {len(data['images'])}")
   print(f"Annotations: {len(data['annotations'])}")
   
   from collections import Counter
   cats = Counter([ann['category_id'] for ann in data['annotations']])
   print("Per-class:", cats)
   ```

2. Document difficulty *(5 min)*
   - Occlusion: none/partial/heavy %
   - Crowd density: sparse/moderate/dense %
   - Scale variation: Describe size range
   - Environmental challenges: List (e.g., "glare", "shadows")

---

### Phase 5: Final Sections (30 minutes)

**Dataset Statistics (10 min)**
- Temporal coverage: Date range, seasons
- Spatial coverage: Number of locations, area
- Class balance: Most vs least common (ratio)

**Limitations and Bias (10 min)**
- Geographic bias? (e.g., "Only protected areas")
- Temporal bias? (e.g., "Morning flights only")
- Species bias? (e.g., "Large animals overrepresented")
- Be honest! This helps users apply your data appropriately

**Licensing (5 min)**
- Confirm your license choice
- Add any special conditions
- Note if images have different licenses than compilation

**Citation (5 min)**
- Fill in BibTeX template with your information
- Include paper DOI if published

---

## Validation

**Before publishing, run through checklist:**

### FAIR² Compliance
- [ ] DOI assigned or pending
- [ ] License clearly stated
- [ ] All required (*) fields completed
- [ ] Machine-readable YAML front matter filled
- [ ] Contact information provided

### Darwin Core Compliance
- [ ] Event records complete (dates, locations, protocol)
- [ ] Occurrence records have scientific names
- [ ] Taxonomic hierarchy filled (at least to family)
- [ ] Sampling effort quantified
- [ ] Coordinates in WGS84 with uncertainty

### Practical Completeness
- [ ] Directory structure documented
- [ ] File naming convention explained
- [ ] Data splits clearly defined
- [ ] Annotation format specified
- [ ] At least one example image linked
- [ ] Known limitations acknowledged

**Use validator tool:**
```bash
python fair2_validate.py --card your_dataset_card.md --level recommended
```

---

## Common Mistakes to Avoid

### 1. **Vague Descriptions**
❌ "We used a drone to collect wildlife images"
✓ "DJI Matrice 300 RTK with Zenmuse H20T camera flew grid patterns at 60m AGL"

### 2. **Missing Geographic Precision**
❌ "Collected in Tanzania"
✓ "Serengeti National Park, Mara Region (-2.3456, 34.8123 ±5m)"

### 3. **Unclear Sampling Effort**
❌ "Multiple flights"
✓ "45 missions totaling 30 flight hours, covering 2,500 hectares"

### 4. **Incomplete Species Names**
❌ "elephants, zebras, giraffes"
✓ "Loxodonta africana, Equus quagga, Giraffa camelopardalis"

### 5. **Undocumented Splits**
❌ "Split into train/val/test"
✓ "Stratified by location and season: missions 1-300 (train), 301-350 (val), 351-400 (test)"

### 6. **Hidden Biases**
❌ "Representative wildlife dataset"
✓ "Dry season only; large-bodied species overrepresented; morning flights bias against nocturnal species"

---

## Time-Saving Tips

### Before You Start:
1. **Gather info first:** Don't start filling the template until you have everything collected
2. **Use existing docs:** Copy from your paper methods section
3. **Check manufacturer sites:** Drone/camera specs are usually available online

### While Filling:
4. **Start with easy sections:** Overview and structure first, build confidence
5. **Leave blanks temporarily:** Mark sections to "ask author" or "calculate later"
6. **Use templates:** Copy-paste structure from example cards

### For Missing Info:
7. **EXIF data is your friend:** Image metadata often has timestamp, GPS, camera settings
8. **Estimate reasonably:** "Approximately 60m altitude" is better than blank
9. **Contact original team:** If retrofitting someone else's dataset
10. **Document what's missing:** "Sensor calibration files not available" is acceptable

---

## Resources (TO DO)

### Validation Tools
- `fair2_template.py` - Generate blank template for your task type
- `fair2_validate.py` - Check completeness
- `fair2_to_dwc.py` - Export Darwin Core records for GBIF
- `fair2_to_hf.py` - Convert to HuggingFace format

### Example Datasets
- KABR: Full multi-task dataset card
- MMLA: Detection-only dataset card

### Templates by Task
- `template_detection.md` - Detection only (minimal)
- `template_tracking.md` - Detection + tracking
- `template_behavior.md` - Detection + behavior
- `template_robotics.md` - Platform-focused

### External Resources
- [Darwin Core Quick Reference](https://dwc.tdwg.org/terms/)
- [GBIF Species Search](https://www.gbif.org/species/search)
- [FAIR² Principles](https://doi.org/10.1038/s41597-023-02298-6)
- [Barnas et al. UAV Protocol](https://doi.org/10.1139/juvs-2019-0011)

---

## Getting Help

**Questions? Issues?**

1. **GitHub Issues:** fair_drones/issues
2. **Discussion Forum:** [link to forum] (WILDLABS)
3. **Email:** fair2-drone@example.org
4. **Office Hours:** [schedule if available]

**Want to contribute?**
- Submit example cards
- Report unclear sections
- Suggest improvements
- Build validation tools

---

**Ready to start?**

1. Download the appropriate template for your task
2. Gather your information (use the 5-minute prep checklist)
3. Set aside 2-3 hours in your calendar
4. Follow this guide section by section
5. Validate your completed card
6. Publish and celebrate your FAIR² compliant dataset! 🎉

