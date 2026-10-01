import pandas as pd
import numpy as np
from pathlib import Path
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from keras.regularizers import l2
from keras.optimizers import Adam

plots_dir = Path(__file__).resolve().parent / 'Plots'
plots_dir.mkdir(parents=True, exist_ok=True)

dataset = pd.read_csv(r"Datafiles/training_dataset.csv")
Validation_set = pd.read_csv(r"Datafiles/validation_dataset.csv")

X = dataset.iloc[:, :-1].values  # All columns except the last one
y = dataset.iloc[:, -1].values*100  # The last column

X_val = Validation_set.iloc[:, :-1].values
y_val = Validation_set.iloc[:, -1].values*100

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = Sequential()
model.add(Dense(128, input_dim=X_train.shape[1], activation='relu',kernel_regularizer=l2(0.0001)))
model.add(Dense(64, activation='relu'))
#Output layer
model.add(Dense(1, activation='relu'))

optimizer = Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, loss='mean_squared_error', metrics=['mae'])
model.summary()

history = model.fit(X_train, y_train, epochs=150,batch_size=16, validation_split=0.2)


from matplotlib import pyplot as plt
#plot the training and validation accuracy and loss at each epoch
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(loss) + 1)
plt.figure()
plt.plot(epochs, loss, 'g', label='Training loss')
plt.plot(epochs, val_loss, 'r', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
plt.close()


acc = history.history['mae']
val_acc = history.history['val_mae']
plt.figure()
plt.plot(epochs, acc, 'y', label='Training MAE')
plt.plot(epochs, val_acc, 'r', label='Validation MAE')
plt.title('Training and validation MAE')
plt.xlabel('Epochs')
plt.ylabel('MAE')
plt.legend()
plt.show()
plt.close()

#Predict on test data
predictions = model.predict(X_val)
print("Predicted values are: ", np.round(predictions,2))
print("Real values are: ", y_val)

mse_neural_test, mae_neural_test = model.evaluate(X_test, y_test)
print('Mean squared error from neural net: ', mse_neural_test)
print('Mean absolute error from neural net: ', mae_neural_test)

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate R^2 value
ss_total = np.sum((y_test - np.mean(y_test)) ** 2)
ss_residual = np.sum((y_test - y_pred.flatten()) ** 2)
r2_score_test = 1 - (ss_residual / ss_total)

print('R^2 score on test set from neural net: ', r2_score_test)


# Save the measured-versus-predicted plot for testing samples.
plt.figure(figsize=(7, 7))
plt.scatter(y_test, y_pred.flatten(), color='blue',
            label=f'Testing Samples : R^2 = {np.round(r2_score_test,4)} , RMSE = {np.round(np.sqrt(mse_neural_test),4)}')
lower = min(np.min(y_test), np.min(y_pred))
upper = max(np.max(y_test), np.max(y_pred))
plt.plot([lower, upper], [lower, upper], color='black', linestyle='--',
         label='Ideal Prediction')
plt.xlabel('Measured Moisture Content (%)')
plt.ylabel('Predicted Moisture Content (%)')
plt.legend()
plt.grid()
plt.savefig(plots_dir / 'neural_network_testing.png', dpi=300)
plt.show()
plt.close()


mse_neural_val, mae_neural_val = model.evaluate(X_val, y_val)
print('Mean squared error from neural net: ', mse_neural_val)
print('Mean absolute error from neural net: ', mae_neural_val)

# Predict on the test set
y_pred_val = model.predict(X_val)

# Calculate R^2 value
ss_total = np.sum((y_val - np.mean(y_val)) ** 2)
ss_residual = np.sum((y_val - y_pred_val.flatten()) ** 2)
r2_score_val = 1 - (ss_residual / ss_total)

print('R^2 score on test set from neural net: ', r2_score_val)


# Plot y_test vs y_pred and y_val vs y_pred_val in the same plot
plt.figure(figsize=(7, 7))

# Scatter plot for test data
# plt.scatter(y_test, y_pred, color='blue', label=f'Testing Samples :  R^2 = {np.round(r2_score_test,4)} ,  RMSE = {np.round(np.sqrt(mse_neural_test),4)}')
# Scatter plot for validation data
plt.scatter(y_val, y_pred_val, color='red', label=f'Validation Samples : R^2 = {np.round(r2_score_val,4)}  ,  RMSE = {np.round(np.sqrt(mse_neural_val),4)}')

# Plot the ideal prediction line
# plt.plot([min(min(y_test), min(y_val)), max(max(y_test), max(y_val))],
#          [min(min(y_test), min(y_val)), max(max(y_test), max(y_val))],
#          color='black', linestyle='--', label='Ideal Prediction')

plt.plot([min(y_val), max(y_val)+8],
         [min(y_val), max(y_val)+8],
         color='black', linestyle='--', label='Ideal Prediction')

plt.xlabel('Measured Moisture Content (%)')
plt.ylabel('Predicted Moisture Content (%)')
# plt.title('2HalfSigma_tanh_steepness_0_04')
plt.legend(fontsize=10.5)
# plt.legend()
plt.grid()
plt.savefig(plots_dir / 'neural_network_validation.png', dpi=300)
plt.show()
plt.close()
