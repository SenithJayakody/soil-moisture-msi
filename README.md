# Deep Learning for Soil Moisture Estimation via Reflectance Multispectral Imaging

> **Published at the 2024 International Conference on Advances in Technology and Computing (ICATC).**

## Overview

This repository accompanies the publication:

**"Deep Learning for Soil Moisture Content Estimation via Reflectance Multispectral Imaging"**

The study presents a rapid, low-cost, and indirect approach for estimating soil moisture content using reflectance multispectral imaging (MSI) combined with a regression neural network.

A custom-built, field-deployable MSI system captures spectral information from soil samples across 13 narrow spectral bands ranging from 365 nm to 940 nm.

## Methodology

The proposed framework consists of:

1. Reflectance multispectral image acquisition
2. Dark-current subtraction
3. Image preprocessing and intensity correction
4. Spectral feature representation
5. Feature normalization
6. Neural-network-based regression
7. Soil moisture content estimation
8. Validation using an independently prepared soil sample

The multispectral imaging system uses the following wavelengths:

`365, 405, 473, 530, 575, 621, 660, 735, 770, 830, 850, 890, and 940 nm`

## Key Results

| Dataset | R² | RMSE |
|---|---:|---:|
| Test data | 0.9987 | 0.5072 |
| Independent validation | 0.9922 | 0.7517 |

The results demonstrate that spectral information acquired using a compact 13-band MSI system can be used for accurate soil moisture content estimation.

## Publication

**Deep Learning for Soil Moisture Content Estimation via Reflectance Multispectral Imaging**

S. Ranasinghe, S. Jayakody, M. De Silva, V. Herath, R. Godaliyadda, M. P. Ekanayake, S. Navaratnarajah, F. Kizel, and G. Thilakarathne

*2024 International Conference on Advances in Technology and Computing (ICATC)*

**DOI:** `10.1109/ICATC64549.2024.11025290`

## Project Timeline

- Research and development: 2024
- Publication: ICATC 2024
- Public repository release: 2026

## Repository Contents

The implementation, preprocessing scripts, model training code, evaluation scripts, and result-reproduction instructions will be added to this repository.

## Code

The complete research implementation will be made available here.

## Data

Dataset availability and expected directory structure will be documented alongside the code release.

## Citation

If you use this work, please cite:

```bibtex
@INPROCEEDINGS{11025290,
  author={Ranasinghe, Sandunika and Jayakody, Senith and Silva, Mario De and Herath, Vijitha and Godaliyadda, Roshan and Ekanayake, Mervyn Parakrama and Navaratnarajah, Sinniah and Kizel, Fadi and Thilakarathne, Gayathri},
  booktitle={2024 International Conference on Advances in Technology and Computing (ICATC)},
  title={Deep Learning for Soil Moisture Content Estimation via Reflectance Multispectral Imaging},
  year={2024},
  pages={1-6},
  doi={10.1109/ICATC64549.2024.11025290}
}
