import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MaxAbsScaler
from sklearn.decomposition import PCA

# Load data
df = pd.read_csv('diabetes.csv')
x = df[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']]
y = df['Outcome']

# Train-test split
x_tr, x_test, y_tr, y_test = train_test_split(x, y, train_size=0.8)
x_val, x_test, y_val, y_test = train_test_split(x_test, y_test, train_size=0.5)

# Preprocessing
scaler = MaxAbsScaler()
x_tr = scaler.fit_transform(x_tr)
x_test = scaler.transform(x_test)
x_val = scaler.transform(x_val)

pca = PCA(n_components=4)
xs_tr = pca.fit_transform(x_tr)
xs_test = pca.transform(x_test)
xs_val = pca.transform(x_val)

import tensorflow as tf
from tensorflow.keras import layers, models

# Build the model
nn_model = models.Sequential([
    layers.Dense(8, activation='relu', input_shape=(xs_tr.shape[1],)),
    layers.Dense(4, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# Compile the model
nn_model.compile(optimizer='adam', 
                 loss='binary_crossentropy', 
                 metrics=['accuracy'])

# Print model summary
nn_model.summary()

# Early stopping callback
earlystop_nn = tf.keras.callbacks.EarlyStopping(
    monitor="val_loss", patience=2, verbose=1, restore_best_weights=True)

# Train the model
nn_history = nn_model.fit(xs_tr, y_tr, epochs=50, batch_size=20, 
                          validation_data=(xs_val, y_val), 
                          callbacks=[earlystop_nn])

# Save NN model weights
# nn_model.save_weights("nn_weight.h5")

# Evaluate on test data
nn_test_loss, nn_test_acc = nn_model.evaluate(xs_test, y_test)
print(f"NN Test Accuracy: {nn_test_acc:.4f}, Test Loss: {nn_test_loss:.4f}")

import matplotlib.pyplot as plt

def plot_losses(nn_history):
    nn_tr_loss = nn_history.history["loss"]
    nn_val_loss = nn_history.history["val_loss"]

    epochs = np.arange(1, len(nn_tr_loss) + 1)
    
    plt.plot(epochs, nn_tr_loss, label="NN Training Loss", linestyle='dashed')
    plt.plot(epochs, nn_val_loss, label="NN Validation Loss", linestyle='dashed')
    
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.show()

plot_losses( nn_history)
