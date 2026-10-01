import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import log
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.preprocessing import MinMaxScaler

# Creating traning dataset
dataset = pd.read_csv('./Datafiles/dataAll_Soil02_06.csv')

i = 0
while i < len(dataset):
    if dataset.iloc[i, 13] <= 0.41:
        level_matrix = dataset.iloc[i:, :14]
        break
    i += 1

print(level_matrix)

features = level_matrix.iloc[:, :-1].values
y_original = level_matrix.iloc[:, -1].values
print(features)

combined_df = pd.DataFrame(features)
combined_df['Target'] = y_original

# Save the combined data to a CSV file
combined_df.to_csv('./Datafiles/training_dataset.csv', index=False)


# Creating validating dataset
dataset = pd.read_csv('./Datafiles/dataAll_Soil02_26.csv')

i = 0
while i < len(dataset):
    if dataset.iloc[i, 13] <= 0.41:
        level_matrix = dataset.iloc[i:, :14]
        break
    i += 1


print(level_matrix)

features = level_matrix.iloc[:, :-1].values
y_original_26 = level_matrix.iloc[:, -1].values
print(features)

combined_df = pd.DataFrame(features)
combined_df['Target'] = y_original_26

# Save the combined data to a CSV file
combined_df.to_csv('./Datafiles/validation_dataset.csv', index=False)





