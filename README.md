# AutoCAF: Automated Feature Extraction from Control Artifacts in GitHub Repositories

## Project Overview

This repository implements the methodology presented in the research paper _"Automated Feature Extraction from Control Artifacts in GitHub Repositories"_ published at the 2024 Systems and Information Engineering Design Symposium (SIEDS), University of Virginia (Scopus-indexed).

The project focuses on parsing and semantically embedding control artifacts from GitHub repositories. Control artifacts — such as GitHub Actions workflows, Dockerfiles, shell scripts, YAML configurations, and other CI/CD-related files — often contain critical information about the operational behavior of software projects. However, they are typically ignored or underutilized in repository mining efforts.

This work introduces a systematic approach to detect these files, analyze their structure, and extract meaningful vectorized representations that can be used for downstream tasks such as repository classification, CI/CD intent modeling, or pipeline recommendation systems.

## Motivation

Modern software repositories increasingly rely on automation, yet research tools and models tend to prioritize application source code over the operational logic embedded in control artifacts. This leaves a gap in how we understand repository behavior, software maturity, and engineering practices. Our approach fills this gap by treating control artifacts as first-class citizens in repository mining.

By automating the extraction of features from these artifacts, we aim to make it easier to conduct large-scale studies on automation usage, detect anti-patterns, or even generate intelligent suggestions for workflow design.

## Core Components

The pipeline implemented in this repository follows these main phases, each designed to work independently or as part of a unified processing flow:

### Artifact Detection

We start by identifying relevant control artifacts in a given GitHub repository. This includes:
- YAML or JSON files under `.github/workflows`, `.circleci/`, `.gitlab-ci.yml`, etc.
- Dockerfiles or container build scripts
- Shell scripts and automation tools like `Makefile`, `Jenkinsfile`, etc.

File detection is performed using a combination of file-path heuristics and pattern-based filters.

### Preprocessing

Once the relevant files are identified, they are preprocessed to normalize variations and reduce noise. This step may include:
- Token normalization (e.g., replacing hardcoded variables with placeholders)
- Removal of comments and environment-specific tokens
- Standardization of control structures (loops, conditions, triggers)

This makes the artifacts easier to model across projects.

### Feature Extraction

The cleaned control artifacts are then transformed into numerical representations using multiple strategies, including:
- Token frequency (bag-of-operations)
- Structural metadata (steps, triggers, runners, containers)
- Language model embeddings (from models pretrained on code/configuration)
- Graph-based representations (for control/data flow structure)

These features are concatenated or used individually depending on the task (e.g., classification, clustering, similarity retrieval).

### Output

The final output is a matrix of feature vectors — one per artifact — suitable for integration with machine learning pipelines. These embeddings can be used for:
- Repository-level classification (e.g., maturity level, DevOps intent)
- Visualization and clustering of automation strategies
- Recommender systems for workflow templates

## System Architecture

Refer to **Figure 2** in the research paper for a high-level architecture diagram of the entire pipeline, including detection, parsing, and embedding stages. This figure serves as a visual summary of the system design and component flow.

## Applications

This framework can be used for a range of practical applications such as:
- Analyzing automation usage trends across open-source ecosystems
- Building developer tools that offer recommendations for CI/CD workflows
- Detecting anti-patterns or misconfigurations in pipeline definitions
- Bootstrapping datasets for large-scale CI/CD research

## Publication

This work was published in the **2024 Systems and Information Engineering Design Symposium (SIEDS)** organized by the University of Virginia and indexed in Scopus.

## Citation

Please cite the original paper if you use this project or build on top of it:

```bibtex
@article{vaghulade2024automated,
  title        = {Automated Feature Extraction from Version Control Artifacts in GitHub Repositories},
  author       = {Vaghulade, Maitreya and Dalal, Urav and Fargose, Sean and Shah, Devang and Maniar, Kush and Bhowmick, Kiran and Narvekar, Meera},
  journal      = {Journal of Electrical Systems},
  volume       = {20},
  number       = {10s},
  pages        = {8246--8252},
  year         = {2024},
  month        = jul,
  doi          = {10.52783/jes.7091},
  url          = {https://doi.org/10.52783/jes.7091}
}
```
## Contact

For questions, suggestions, or collaborations, feel free to open an issue or reach out via maitreya.vaghulade@gmail.com
