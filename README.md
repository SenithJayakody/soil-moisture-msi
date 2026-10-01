# Deep Learning for Soil Moisture Content Estimation via Reflectance Multispectral Imaging

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
5. Preparation of training and independent validation datasets
6. Neural-network-based regression
7. Soil moisture content estimation
8. Validation using an independently prepared soil sample

The multispectral imaging system uses the following wavelengths:

`365, 405, 473, 530, 575, 621, 660, 735, 770, 830, 850, 890, and 940 nm`

## Published Results

| Dataset | R² | RMSE |
|---|---:|---:|
| Test data | 0.9987 | 0.5072 |
| Independent validation | 0.9922 | 0.7517 |

These values are reported in the publication; they have not been reproduced from this repository. The current training script does not set a neural-network random seed, so results may vary between runs.

## Publication

**Deep Learning for Soil Moisture Content Estimation via Reflectance Multispectral Imaging**

S. Ranasinghe, S. Jayakody, M. De Silva, V. Herath, R. Godaliyadda, M. P. Ekanayake, S. Navaratnarajah, F. Kizel, and G. Thilakarathne

*2024 International Conference on Advances in Technology and Computing (ICATC)*

**DOI:** `10.1109/ICATC64549.2024.11025290`

## Project Timeline

- Research and development: 2024
- Publication: ICATC 2024
- Public repository release: 2026

## Repository Structure

The Python scripts are included in the repository. `Images/`, `Datafiles/`, and `Plots/` below describe the expected local input and output folders; they are not currently included.

```text
soil-moisture-msi/
|-- README.md
|-- LICENSE
|-- .gitignore
|-- Make_Datafiles.py
|-- Create_train_and_validation_datasets.py
|-- Regression_neural_network.py
|-- Spectral_signature_&_parabola_plot.py
|-- Images/                              # User-supplied image captures
|   |-- <sample-group>/                  # Separate groups for cups 06 and 26
|       |-- <cup>_<level>_<subsample>/    # Capture name, e.g. 06_01_A
|           |-- 000nm.png                # Dark-current reference
|           |-- 365nm.png
|           |-- ...                      # One image per wavelength listed above
|           |-- 940nm.png
|-- Datafiles/                           # Generated CSV files
|   |-- dataAll_Soil02_06.csv
|   |-- dataAll_Soil02_26.csv
|   |-- training_dataset.csv
|   |-- validation_dataset.csv
|-- Plots/                               # Generated figures
    |-- neural_network_testing.png
    |-- neural_network_validation.png
    |-- Spectral Signature - Validation_dataset.png
    |-- Parabola Plot - Validation_dataset.png
```

| Script | Purpose |
|---|---|
| `Make_Datafiles.py` | Subtracts the dark-current image, applies intensity correction to a 100 x 100 pixel region, and extracts 13-band features from 100 patches per capture. |
| `Create_train_and_validation_datasets.py` | Creates datasets for cups 06 and 26, keeping rows from the first moisture content at or below 0.41 onward. |
| `Regression_neural_network.py` | Trains a regression network, evaluates the test and independent validation sets, and saves measured-versus-predicted plots. |
| `Spectral_signature_&_parabola_plot.py` | Groups the validation data by moisture content and saves spectral signatures and intensity-versus-moisture plots for selected wavelengths. |

## Requirements

The scripts use Python with NumPy, pandas, Matplotlib, OpenCV (`opencv-python`), scikit-learn, and Keras with a compatible backend such as TensorFlow.

A tested environment or pinned dependency file is not yet provided. `Regression_neural_network.py` imports the legacy `keras.wrappers.scikit_learn.KerasRegressor` module, even though it does not use it. The chosen Keras version must provide that module, or the unused import must be removed before using an environment that does not provide it.

## Data Preparation

Raw images, prepared datasets, and trained model weights are not included. Supply your own captures under `Images/` using the layout above, or provide compatible CSV files under `Datafiles/` to start at a later step.

Each capture needs a grayscale dark-current reference (`000nm.png`) and all 13 wavelength images. The extraction script crops rows 700-799 and columns 475-574, so images must cover that region.

The moisture labels are hardcoded for cups `06` and `26`. Capture folders use `<cup>_<level>_<subsample>`, with subsamples `A`, `B`, and `C`. The script assigns labels using a counter advanced by each `A` capture and processes folders in filesystem enumeration order. Verify that this order matches the hardcoded moisture-label sequence before generating data; the numeric level in the folder name is not used to select the label.

Extracted CSV files contain the 13 wavelength columns followed by `Moisture Content`, expressed as a fraction. Prepared datasets contain feature columns `0` through `12` followed by `Target`. The regression script converts targets to percentages by multiplying them by 100; it does not apply feature normalization.

## Running the Scripts

Run these commands from the repository root after preparing the images and installing compatible dependencies:

```powershell
python Make_Datafiles.py
python Create_train_and_validation_datasets.py
python Regression_neural_network.py
python "Spectral_signature_&_parabola_plot.py"
```

If the two extracted CSV files already exist, start with the second command. If the prepared training and validation datasets already exist, start with the third command.

The plotting script currently reads `Datafiles/Validation_dataset.csv`, while the dataset creation script writes `Datafiles/validation_dataset.csv`. On a case-sensitive filesystem, change `CSV_PATH` in the plotting script to match the generated lowercase filename before running it.

The regression network has hidden layers of 128 and 64 units and a single output unit. It uses an 80/20 training/test split, reserves 20% of the training portion for validation during fitting, and trains for 150 epochs with a batch size of 16. Cup 26 supplies the independent validation dataset.

Figures are saved under `Plots/`. The regression script also opens interactive plot windows and prints evaluation metrics; it does not save the trained model.

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
