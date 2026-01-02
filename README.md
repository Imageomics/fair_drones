# FAIR² Drone Data Standard

**A unified metadata standard for drone-based wildlife datasets**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

---

## Overview

The FAIR² Drone Data Standard provides a comprehensive framework for documenting drone-based wildlife datasets, ensuring they are **Findable, Accessible, Interoperable, and Reusable** while maintaining compliance with Darwin Core biodiversity data standards. This standard bridges ecology, robotics, and computer vision communities by providing unified metadata specifications that enable cross-domain dataset reuse.

## Purpose

Field data collection using aerial and underwater drones represents substantial investment in time, expertise, and resources. However, most datasets serve only single research communities, limiting interdisciplinary potential. The FAIR² standard addresses this by:

- **Standardizing metadata** across ecology, robotics, and computer vision domains
- **Integrating Darwin Core** biodiversity standards for ecological compliance
- **Documenting platform specifications** essential for robotics research
- **Specifying annotation formats** required for AI/ML applications
- **Enabling multimodal linkages** to complementary sensor data

## Key Features

- **Modular template system** supporting detection, tracking, behavior recognition, and robotics benchmarking
- **Darwin Core compliance** with Event and Occurrence records for GBIF integration
- **Comprehensive platform metadata** including telemetry, sensors, and mission parameters
- **Multi-task annotation support** for object detection, tracking, segmentation, and behavior analysis
- **Validation tools** for ensuring standard compliance
- **Reference implementations** demonstrating real-world applications

## Repository Contents

- **[TEMPLATE.md](TEMPLATE.md)**: Full dataset card template with detailed field descriptions
- **[QUICKSTART_GUIDE.md](QUICKSTART_GUIDE.md)**: Checklist-based guide for rapid implementation
- **[examples/](examples/)**: Reference implementations on real-world datasets
  - **[KABR Behavior Telemetry](https://github.com/Imageomics/kabr-behavior-telemetry)**: Complete example with GPS extraction, Darwin Core events, and processing scripts
- **Validation scripts**: Tools for checking standard compliance (coming soon)

## Getting Started

1. **Review the [Quick-Start Guide](QUICKSTART_GUIDE.md)** for a checklist-based approach
2. **Select your template** based on primary use case (detection, tracking, behavior, robotics)
3. **Complete the dataset card** following the [full template](TEMPLATE.md)
4. **Validate compliance** using provided tools
5. **Publish your dataset** with FAIR² documentation

Estimated completion time: 2-4 hours depending on dataset complexity

## Standard Components

### Core Metadata
- Dataset identification and attribution
- Licensing and citation information
- Data structure and file organization
- Dataset splits and statistics

### Darwin Core Integration
- Event records (survey locations, dates, protocols)
- Occurrence records (species observations, taxonomic hierarchy)
- Sampling effort and coverage metrics
- Geographic coordinates with uncertainty

### Platform Specifications
- UAV/UUV hardware details
- Sensor specifications (camera, thermal, LiDAR, etc.)
- Flight parameters and telemetry
- Autonomy modes and mission planning

### Annotation Documentation
- Task-specific formats (COCO, MOT, ethograms)
- Quality metrics and inter-annotator agreement
- Annotation difficulty and coverage statistics
- Label sets and class distributions

## Common Workflows

Many datasets require processing raw telemetry and metadata before documentation:

1. **GPS Extraction**: Extract coordinates from flight logs (SRT files, EXIF data, telemetry logs)
2. **Event Aggregation**: Aggregate video-level data to mission/session-level Darwin Core events
3. **Occurrence Generation**: Link species detections to biodiversity occurrence records
4. **Statistics Calculation**: Compute coverage metrics, annotation counts, and class distributions

See the [KABR processing scripts](https://github.com/Imageomics/kabr-behavior-telemetry/tree/main/scripts) for Python examples of GPS extraction, event aggregation, and Darwin Core generation.

## Target Audiences

- **Ecologists**: Documenting wildlife surveys for biodiversity databases and research publications
- **Computer Vision Researchers**: Creating benchmark datasets for algorithm development
- **Robotics Engineers**: Developing autonomous systems and testing perception pipelines
- **Conservation Practitioners**: Sharing monitoring data across organizations
- **Data Scientists**: Training and evaluating machine learning models

## Citation

If you use this standard or template, please cite:

```bibtex
@misc{fair2_drone_standard,
  title={FAIR² Drone Data Standard for Wildlife Datasets},
  author={[Authors]},
  year={2025},
  publisher={GitHub},
  howpublished={\\url{https://github.com/Imageomics/fair_drones}}
}
```

## Contributing

We welcome contributions to improve and extend this standard:

- Report issues or unclear documentation via [GitHub Issues](https://github.com/Imageomics/fair_drones/issues)
- Submit example dataset cards
- Propose extensions for additional domains or modalities
- Contribute validation tools and utilities

## License

This standard and documentation are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Acknowledgements

This work builds upon:
- [FAIR Principles](https://doi.org/10.1038/sdata.2016.18) for scientific data management
- [Darwin Core](https://dwc.tdwg.org/) biodiversity data standards
- [Hugging Face Dataset Cards](https://huggingface.co/docs/hub/datasets-cards) for ML datasets
- [Imageomics Dataset Card Template](https://imageomics.github.io/Imageomics-guide/wiki-guide/HF_DatasetCard_Template_Imageomics/) for biodiversity and computer vision dataset documentation
- UAV best practices from [Barnas et al. 2020](https://doi.org/10.1139/juvs-2019-0011)

## Support

For questions, comments, or concerns:
- Open an issue on [GitHub](https://github.com/Imageomics/fair_drones/issues)
- Refer to the [Quick-Start Guide](QUICKSTART_GUIDE.md) for implementation guidance
- Review [example implementations](examples/) for reference

---

**Project Status**: Active development | Version 1.0 (2025)
