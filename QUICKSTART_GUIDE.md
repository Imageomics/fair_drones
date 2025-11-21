# FAIR² Drone Dataset Card: Quick-Start Guide

**For researchers creating or documenting drone-based wildlife datasets**

Below is a streamlined checklist for creating a FAIR² compliant drone dataset card. Review the full [dataset card template](TEMPLATE.md) for detailed guidance.

!!! tip "Pro tip"

    Use the eye icon at the top of this page to access the source and copy the markdown for the checklist below into an issue on your GitHub repository so you can check the boxes as you complete each section.

---

## Before You Start

- [ ] Gather image/video files and annotation files (if applicable)
- [ ] Collect drone/sensor specifications (model numbers)
- [ ] Locate flight logs or mission notes
- [ ] Find research permits and approval numbers
- [ ] Create species list with scientific names (use [GBIF](https://www.gbif.org/species/search))
- [ ] Set aside 2-3 hours for completion

---

## Choose Your Template

Select the appropriate template based on your primary use case:

- **Object Detection**: Detection Template (~2 hours) - Core + Darwin Core + COCO annotations
- **Multi-Object Tracking**: Tracking Template (~2.5 hours) - Detection + MOT format + ID protocols
- **Behavior Recognition**: Behavior Template (~3 hours) - Detection + Ethogram + temporal labels
- **Robotics Benchmarking**: Platform Template (~2.5 hours) - Core + Full telemetry + Minimal annotations
- **Multiple Tasks**: Comprehensive Template (~3-4 hours) - All modules

---

## YAML Front Matter

- [ ] **License**: Specify license type (e.g., `cc-by-4.0`)
- [ ] **Pretty Name**: Provide descriptive dataset name
- [ ] **Task Categories**: List relevant tasks (e.g., `object-detection`, `image-classification`)
- [ ] **Tags**: Include relevant tags (e.g., `wildlife-monitoring`, species names, locations)
- [ ] **Size Categories**: Specify dataset size (e.g., `n<1k`, `1k<n<10k`)

---

## Dataset Overview

- [ ] **Title**: Clear, descriptive title
- [ ] **Description**: 2-3 paragraph summary of dataset purpose and content
- [ ] **Authors**: List curators/authors with affiliations
- [ ] **Contact Information**: Provide contact details or point to discussion forum
- [ ] **Repository**: Link to GitHub repository
- [ ] **Homepage**: Provide link if available
- [ ] **DOI**: Assign or note as pending

---

## Data Structure

- [ ] **Directory Structure**: Document file organization with tree diagram
- [ ] **File Formats**: List formats for images (e.g., JPG, PNG) and annotations (e.g., COCO JSON, YOLO)
- [ ] **Naming Convention**: Explain file naming pattern with examples
- [ ] **Data Splits**: Describe train/val/test splits with counts and creation method
- [ ] **Example Files**: Link to at least one representative image

---

## Darwin Core Metadata

### Event Records

For each survey location/date, document:

- [ ] **eventID**: Unique identifier per mission
- [ ] **eventDate**: Date in ISO format (YYYY-MM-DD)
- [ ] **eventTime**: Time with timezone
- [ ] **decimalLatitude/Longitude**: Coordinates in WGS84
- [ ] **coordinateUncertaintyInMeters**: GPS accuracy (typically 5-10m)
- [ ] **locality**: Study site description
- [ ] **habitat**: Habitat type
- [ ] **samplingProtocol**: Survey method (e.g., "UAV transect at 60m AGL")
- [ ] **sampleSizeValue/Unit**: Coverage area and units
- [ ] **samplingEffort**: Duration or effort metric

### Occurrence Records

- [ ] **Scientific Names**: Verify all species names with authority via [GBIF](https://www.gbif.org/species/search)
- [ ] **Taxonomic Hierarchy**: Complete Kingdom, Phylum, Class, Order, Family, Genus, Species for each taxon
- [ ] **Occurrence Table**: Create table linking events to species observations

---

## Platform Specifications

- [ ] **Platform Type**: Drone type (multirotor, fixed-wing, hybrid)
- [ ] **Manufacturer and Model**: Full platform identification
- [ ] **Physical Specs**: Weight, dimensions, flight time, max speed, wind resistance
- [ ] **Sensor Details**: Camera manufacturer, model, resolution, sensor size, focal length, field of view
- [ ] **Additional Sensors**: List any thermal, LiDAR, multispectral sensors
- [ ] **Gimbal**: Type and axes of stabilization
- [ ] **Autonomy Mode**: Manual, waypoint, or fully autonomous
- [ ] **Flight Features Used**: Grid, orbit, follow, terrain-following, etc.

---

## Mission Parameters

- [ ] **Flight Altitude**: Range in meters AGL
- [ ] **Flight Speed**: Speed in m/s
- [ ] **Flight Pattern**: Description (grid, transect, adaptive)
- [ ] **Coverage**: Area covered per mission
- [ ] **Image Overlap**: Forward/side overlap percentages
- [ ] **Environmental Conditions**: Weather, temperature, wind, visibility
- [ ] **Telemetry Data**: Available flight logs and formats (GPS, IMU, battery, etc.)
- [ ] **Permits**: Research permits, IRB/IACUC approvals, aviation regulations followed
- [ ] **Animal Welfare**: Minimum altitudes, disturbance protocols

---

## Annotations

### Format and Coverage

- [ ] **Supported Tasks**: Detection, tracking, segmentation, behavior, re-ID, keypoints
- [ ] **Annotation Format**: Specify format for each task (COCO, MOT, etc.)
- [ ] **Label Set**: List all classes/species, behaviors, attributes
- [ ] **Total Counts**: Images, annotations, annotations per image (min/max/avg)
- [ ] **Per-Class Distribution**: Count per class/species

### Quality Metrics

- [ ] **Creation Method**: Manual, semi-automatic, or automatic
- [ ] **Annotation Tool**: Software used (CVAT, Label Studio, etc.)
- [ ] **Annotators**: Who created annotations (experts, students, crowd workers)
- [ ] **Quality Assurance**: Number of annotators, inter-annotator agreement, review process
- [ ] **Confidence Scores**: Whether included in annotation files
- [ ] **Known Issues**: Annotation gaps, difficult cases, systematic biases

### Annotation Difficulty

- [ ] **Occlusion**: Percentage of instances with none/partial/heavy occlusion
- [ ] **Crowd Density**: Distribution across sparse/moderate/dense scenarios
- [ ] **Scale Variation**: Range of object sizes
- [ ] **Environmental Challenges**: Glare, shadows, motion blur, etc.

---

## Dataset Statistics

- [ ] **Temporal Coverage**: Date range, seasons represented
- [ ] **Spatial Coverage**: Number of locations, total area surveyed
- [ ] **Class Balance**: Distribution across classes/species
- [ ] **Baseline Results**: Performance metrics if available

---

## Limitations and Considerations

- [ ] **Known Biases**: Geographic, temporal, species, environmental
- [ ] **Limitations**: Technical constraints, coverage gaps, quality issues
- [ ] **Recommendations**: Guidance for appropriate dataset use
- [ ] **Ethical Considerations**: Privacy, animal welfare, cultural sensitivities
- [ ] **Reporting Issues**: Link to issue tracker or community forum

---

## Licensing

- [ ] **License Details**: Confirm license choice and any special conditions
- [ ] **Component Licenses**: Note if images, annotations, or code have different licenses
- [ ] **Attribution Requirements**: Specify how to cite the dataset

---

## Citation

- [ ] **Dataset Citation**: Provide BibTeX entry for the dataset
- [ ] **Associated Paper**: Include citation for related publications

---

## Acknowledgements

- [ ] **Funding Sources**: List grants and funding agencies
- [ ] **Contributors**: Acknowledge field teams, annotators, collaborators
- [ ] **Institutional Support**: Note supporting organizations

---

## Optional Sections

- [ ] **Glossary**: Define technical terms or specialized calculations
- [ ] **Additional Information**: Any other relevant context
- [ ] **Related Datasets**: Links to complementary datasets
- [ ] **Multimodal Linkages**: Connections to other sensor data

---

## Validation Checklist

### FAIR² Compliance

- [ ] DOI assigned or pending
- [ ] License clearly stated
- [ ] All required (*) fields completed in template
- [ ] Machine-readable YAML front matter filled
- [ ] Contact information provided

### Darwin Core Compliance

- [ ] Event records complete (dates, locations, protocol)
- [ ] Occurrence records have scientific names with authorities
- [ ] Taxonomic hierarchy filled (minimum to family level)
- [ ] Sampling effort quantified
- [ ] Coordinates in WGS84 with uncertainty

### Practical Completeness

- [ ] Directory structure documented
- [ ] File naming convention explained
- [ ] Data splits clearly defined
- [ ] Annotation format specified
- [ ] At least one example image linked
- [ ] Known limitations acknowledged

---

## Common Mistakes to Avoid

**Vague Descriptions**
❌ "We used a drone to collect wildlife images"
✓ "DJI Matrice 300 RTK with Zenmuse H20T camera flew grid patterns at 60m AGL"

**Missing Geographic Precision**
❌ "Collected in Tanzania"
✓ "Serengeti National Park, Mara Region (-2.3456, 34.8123 ±5m)"

**Unclear Sampling Effort**
❌ "Multiple flights"
✓ "45 missions totaling 30 flight hours, covering 2,500 hectares"

**Incomplete Species Names**
❌ "elephants, zebras, giraffes"
✓ "Loxodonta africana, Equus quagga, Giraffa camelopardalis"

**Undocumented Splits**
❌ "Split into train/val/test"
✓ "Stratified by location and season: missions 1-300 (train), 301-350 (val), 351-400 (test)"

**Hidden Biases**
❌ "Representative wildlife dataset"
✓ "Dry season only; large-bodied species overrepresented; morning flights bias against nocturnal species"

---

## Time-Saving Tips

**Before Starting:**
- Gather all information before opening the template
- Copy from existing paper methods sections
- Look up drone/camera specs online from manufacturer sites

**While Completing:**
- Start with easy sections (Overview, Structure) to build momentum
- Mark sections to revisit with TODO notes
- Use EXIF data from images for missing camera/GPS information
- Estimate reasonably if exact values unavailable (note as approximations)

**For Missing Information:**
- Document what's unavailable rather than leaving blank
- Contact original research team if retrofitting dataset
- Use "not available" or "not recorded" explicitly

---

## Resources

### Validation Tools
- Python scripts for template generation and validation (coming soon)
- Darwin Core export tools for GBIF submission
- HuggingFace conversion utilities

### External Resources
- [Darwin Core Quick Reference](https://dwc.tdwg.org/terms/)
- [GBIF Species Search](https://www.gbif.org/species/search)
- [FAIR² Principles Paper](https://doi.org/10.1038/s41597-023-02298-6)
- [UAV Best Practices (Barnas et al.)](https://doi.org/10.1139/juvs-2019-0011)

---

## Getting Help

!!! question "[Questions, Comments, or Concerns?](https://github.com/Imageomics/fair_drones/issues)"

For assistance:
- Report issues or unclear sections via GitHub Issues
- Contribute example cards or improvements
- Share feedback on the template

---

**Ready to start?**

1. Download the appropriate template for your task
2. Gather your information using the checklist above
3. Set aside 2-3 hours to complete the card
4. Follow the template section by section
5. Validate your completed card
6. Publish your FAIR² compliant dataset!
