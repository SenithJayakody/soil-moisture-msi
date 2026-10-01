import os
import numpy as np
import cv2
import pandas as pd
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
MainPath = PROJECT_DIR / "Images"
OutputPath = PROJECT_DIR / "Datafiles"

OutputPath.mkdir(parents=True, exist_ok=True)

moisture_content = [
    [
        0.78,
        0.77,
        0.75,
        0.72,
        0.70,
        0.67,
        0.65,
        0.63,
        0.61,
        0.58,
        0.54,
        0.50,
        0.49,
        0.46,
        0.44,
        0.40,
        0.36,
        0.32,
        0.27,
        0.23,
        0.16,
        0.13,
        0.07,
        0.04,
        0.02,
        0.00,
    ],
    [
        0.80,
        0.66,
        0.52,
        0.27,
        0.23,
        0.18,
        0.16,
        0.12,
        0.09,
        0.06,
        0.04,
        0.00,
    ],   
]

moisture_by_cup ={
    "06": moisture_content[0],
    "26": moisture_content[1],
}

wavelengths = [
    "365",
    "405",
    "473",
    "530",
    "575",
    "621",
    "660",
    "735",
    "770",
    "830",
    "850",
    "890",
    "940",
]

regions = [700, 800, 475, 575]  # Y1, Y2, X1, X2

subdirList = [
    d for d in os.listdir(MainPath) if os.path.isdir(os.path.join(MainPath, d))
]
for subdir in subdirList:
    soil_path = MainPath / subdir
    subdirList_2 = [
        d for d in os.listdir(soil_path) if os.path.isdir(os.path.join(soil_path, d))
    ]

    tt = 0
    dataAll_array = np.array([])
    kk = 0

    for subdir_1 in subdirList_2:
        capture_path = soil_path / subdir_1
        # print(subdir_1)

        data = np.zeros((100, 14))

        parts = subdir_1.split("_")

        cup = parts[0]
        level = parts[1]
        subSample = parts[2]

        if subSample == 'A':
            subSampleNum = 1
            tt += 1
        elif subSample == 'B':
            subSampleNum = 2
        else:
            subSampleNum = 3

        y1, y2, x1, x2 = regions

        img_name = capture_path / "000nm.png"
        base_image = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)

        for i in range(len(wavelengths)):
            img_name = os.path.join(capture_path, f"{wavelengths[i]}nm.png")
            image1 = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
            image = cv2.subtract(image1, base_image)

            t = 0

            crop_img1 = image[y1:y2, x1:x2].astype(np.float32)
            avg1 = np.mean(crop_img1)
            std1 = np.std(crop_img1)
            steepness = 0.04

            corrected_img1 = (avg1 - std1 / 2) + std1 * (np.tanh(steepness * (crop_img1 - avg1)) + 1) / 2

            for k in range(10):
                for j in range(10):
                    a = 10 * k
                    b = 10 * j
                    avg_mat = corrected_img1[b : b + 10, a : a + 10]
                    avg = np.mean(avg_mat)
                    data[t, i] = avg
                    t += 1

        data = np.clip(data, 0, 255)

        for t in range(data.shape[0]):
            data[t, 13] = moisture_by_cup[cup][tt - 1]
            # data[t, 14] = degree_of_saturation[kkk][tt - 1]

        if kk == 0:
            dataAll_array = data
            kk = 1
        else:
            dataAll_array = np.vstack((dataAll_array, data))

    column_names = [
        "365",
        "405",
        "473",
        "530",
        "575",
        "621",
        "660",
        "735",
        "770",
        "830",
        "850",
        "890",
        "940",
        "Moisture Content"
    ]

    df = pd.DataFrame(dataAll_array, columns=column_names)

    varName = OutputPath / f"dataAll_Soil02_{cup}.csv"
    df.to_csv(varName, index=False, float_format="%.4f")
    print()