from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


PROJECT_PATH = Path(__file__).resolve().parent
CSV_PATH = PROJECT_PATH / "Datafiles" / "Training_dataset.csv"
PLOTS_PATH = PROJECT_PATH / "Plots"

WAVELENGTHS = [365, 405, 473, 530, 575, 621, 660, 735, 770, 830, 850, 890, 940]
SELECTED_WAVELENGTHS = [473, 735, 830, 850]

# Keep this color list unchanged from Parabol_plot.ipynb.
colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (0, 255, 255),
    (255, 0, 255),
    (192, 192, 192),
    (128, 128, 128),
    (128, 0, 0),
    (128, 128, 0),
    (0, 128, 0),
    (128, 0, 128),
    (0, 128, 128),
    (0, 0, 128),
    (255, 165, 0),
    (255, 192, 203),
    (255, 215, 0),
    (173, 216, 230),
    (240, 230, 140),
    (144, 238, 144),
    (210, 105, 30),
    (75, 0, 130),
    (255, 20, 147),
    (70, 130, 180),
    (245, 222, 179),
    (50, 205, 50),
    (255, 69, 0),
]


def load_and_group_data(csv_path):
    dataframe = pd.read_csv(csv_path)

    wavelength_names = [str(wavelength) for wavelength in WAVELENGTHS]
    numbered_names = [str(index) for index in range(len(WAVELENGTHS))]

    if all(name in dataframe.columns for name in wavelength_names):
        source_columns = wavelength_names
    elif all(name in dataframe.columns for name in numbered_names):
        source_columns = numbered_names
    else:
        raise ValueError(
            "The CSV must contain either wavelength columns 365...940 "
            "or feature columns 0...12."
        )

    if "Moisture Content" in dataframe.columns:
        target_column = "Moisture Content"
    elif "Target" in dataframe.columns:
        target_column = "Target"
    else:
        raise ValueError(
            "The CSV must contain a 'Moisture Content' or 'Target' column."
        )

    selected = dataframe[source_columns + [target_column]].copy()
    selected.columns = wavelength_names + ["Moisture Content"]
    selected = selected.apply(pd.to_numeric, errors="coerce")

    if selected.isna().any().any():
        bad_rows = selected.index[selected.isna().any(axis=1)].tolist()
        raise ValueError(f"The CSV contains missing or non-numeric data in rows: {bad_rows[:10]}")

    grouped = (
        selected.groupby("Moisture Content", as_index=False)[wavelength_names]
        .mean()
        .sort_values("Moisture Content")
    )

    if grouped.empty:
        raise ValueError("The CSV does not contain any data rows.")

    return grouped


def plot_spectral_signatures(grouped, csv_path, plots_path):
    wavelength_names = [str(wavelength) for wavelength in WAVELENGTHS]
    figure, axis = plt.subplots(figsize=(15, 8))

    for index, row in grouped.reset_index(drop=True).iterrows():
        color = tuple(channel / 255.0 for channel in colors[index % len(colors)])
        axis.plot(
            WAVELENGTHS,
            row[wavelength_names].to_numpy(dtype=float),
            marker="o",
            color=color,
            markersize=4,
            linestyle="-",
            linewidth=0.5,
            label=f"{row['Moisture Content'] * 100:.1f}",
        )

    # axis.set_title(f"Spectral Signature - {csv_path.stem}")
    axis.set_xlabel("Wavelength (nm)")
    axis.set_ylabel("Average pixel intensity")
    axis.legend(title="Moisture content", loc="upper left")
    axis.grid(True)
    figure.tight_layout()

    output_path = plots_path / f"Spectral Signature - {csv_path.stem}.png"
    figure.savefig(output_path, dpi=1000, bbox_inches="tight")
    plt.close(figure)
    return output_path


def plot_parabola(grouped, csv_path, plots_path):
    figure, axes = plt.subplots(2, 2, figsize=(10, 8))
    moisture = grouped["Moisture Content"].to_numpy(dtype=float)
    plot_styles = ["r-o", "g--s", "b:^", "m-.d"]

    for axis, wavelength, style in zip(
        axes.flat, SELECTED_WAVELENGTHS, plot_styles
    ):
        intensity = grouped[str(wavelength)].to_numpy(dtype=float)
        axis.plot(moisture, intensity, style, markersize=5)
        axis.set_title(f"{wavelength} nm")
        axis.set_xlabel("Moisture content")
        axis.set_ylabel("Average pixel intensity")
        axis.grid(True)

    # axis.set_title(f"Parabola Plot - {csv_path.stem}")
    # figure.suptitle(f"Parabola Plot - {csv_path.stem}", fontsize=16)
    figure.tight_layout(rect=[0, 0, 1, 0.95])

    output_path = plots_path / f"Parabola Plot - {csv_path.stem}.png"
    figure.savefig(output_path, dpi=1000, bbox_inches="tight")
    plt.close(figure)
    return output_path


def main():
    if not CSV_PATH.is_file():
        raise FileNotFoundError(f"CSV file not found: {CSV_PATH}")
    if CSV_PATH.suffix.lower() != ".csv":
        raise ValueError(f"Input must be a CSV file: {CSV_PATH}")

    PLOTS_PATH.mkdir(parents=True, exist_ok=True)

    grouped = load_and_group_data(CSV_PATH)
    spectral_path = plot_spectral_signatures(grouped, CSV_PATH, PLOTS_PATH)
    parabola_path = plot_parabola(grouped, CSV_PATH, PLOTS_PATH)

    print(f"Saved spectral-signature plot: {spectral_path}")
    print(f"Saved parabola plot: {parabola_path}")


if __name__ == "__main__":
    main()
