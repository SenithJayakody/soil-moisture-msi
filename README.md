# Deep Learning for Soil Moisture Content Estimation via Reflectance Multispectral Imaging

> **Publication:** 2024 International Conference on Advances in Technology and Computing (ICATC).
>
> **Code release:** 2026 · [Paper / DOI](https://doi.org/10.1109/ICATC64549.2024.11025290) · [MIT License](LICENSE)

## Overview

This repository contains code for estimating soil moisture content using reflectance multispectral imaging across 13 spectral bands (365-940 nm) and a regression neural network.

## Key Results

The publication reports the following soil moisture estimation results:

| Dataset | R² | RMSE |
|---|---:|---:|
| Test data | 0.9987 | 0.5072 |
| Independent validation | 0.9922 | 0.7517 |

## Publication

**Deep Learning for Soil Moisture Content Estimation via Reflectance Multispectral Imaging**

S. Ranasinghe, S. Jayakody, M. De Silva, V. Herath, R. Godaliyadda, M. P. Ekanayake, S. Navaratnarajah, F. Kizel, and G. Thilakarathne

*2024 International Conference on Advances in Technology and Computing (ICATC)*

**DOI:** [10.1109/ICATC64549.2024.11025290](https://doi.org/10.1109/ICATC64549.2024.11025290)

## Repository Structure

```text
soil-moisture-msi/
|-- README.md
|-- LICENSE
|-- .gitignore
|-- Make_Datafiles.py
|-- Create_train_and_validation_datasets.py
|-- Regression_neural_network.py
|-- Spectral_signature_&_parabola_plot.py
|-- Images/       # Multispectral image captures
|-- Datafiles/    # Extracted features and prepared datasets
|-- Plots/        # Generated figures
```

`Images/`, `Datafiles/`, and `Plots/` are local input/output folders and are not included in the repository.

| Script | Purpose |
|---|---|
| `Make_Datafiles.py` | Extracts spectral features from multispectral images. |
| `Create_train_and_validation_datasets.py` | Prepares training and validation datasets. |
| `Regression_neural_network.py` | Trains and evaluates the regression network. |
| `Spectral_signature_&_parabola_plot.py` | Generates spectral signature and intensity-versus-moisture plots. |

## Getting Started

### 1. Environment Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On Linux or macOS, activate it with `source .venv/bin/activate`.

Dependencies: NumPy, pandas, Matplotlib, OpenCV, scikit-learn, and Keras with TensorFlow.

The training script requires the legacy Keras scikit-learn wrapper; remove its unused import if your Keras version does not provide it.

### 2. Data Availability

The dataset used in this study is available from the authors upon reasonable request.

### 3. Run the Pipeline

After obtaining the dataset and installing compatible dependencies, run from the repository root:

```powershell
python Make_Datafiles.py
python Create_train_and_validation_datasets.py
python Regression_neural_network.py
python "Spectral_signature_&_parabola_plot.py"
```

Figures are saved under `Plots/`.

On case-sensitive filesystems, update the plotting script's `CSV_PATH` to `Datafiles/training_dataset.csv` to match the generated filename.

## License

The code is distributed under the [MIT License](LICENSE).

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
```
