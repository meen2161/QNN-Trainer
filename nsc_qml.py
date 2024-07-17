import pennylane as qml
import numpy as np
import tensorflow as tf

import keras

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import MaxAbsScaler


from sklearn.decomposition import PCA
from itertools import combinations

tf.keras.backend.set_floatx('float64')
nqubits = 4

def ZZFeatureMap(nqubits, data):
    
    nload = min(len(data), nqubits)
    for i in range(nload):
        qml.Hadamard(i)
        qml.RZ(2.0 * data[:, i], wires = i)
    for pair in list(combinations(range(nload), 2)):
        q0 = pair[0]
        q1 = pair[1]
        qml.CZ(wires = [q0, q1])
        qml.RZ(2.0 * (np.pi- data[:, q0]) * (np.pi- data[:, q1]), wires = q1)
        qml.CZ(wires = [q0, q1])


def TwoLocal(nqubits, theta, reps = 1):
    
    for r in range(reps):
        for i in range(nqubits):
            qml.RY(theta[r * nqubits + i], wires = i)
        for i in range(nqubits - 1):
            qml.CNOT(wires = [i, i + 1])
    
    for i in range(nqubits):
        qml.RY(theta[reps * nqubits + i], wires = i)


def qnn_circuit(inputs, theta):
    global nqubits
    ZZFeatureMap(nqubits, inputs)
    TwoLocal(nqubits = nqubits, theta = theta, reps = 1)
    return qml.expval(qml.Hermitian(M, wires = [0]))


x,y = load_breast_cancer(return_X_y = True)

x_tr, x_test, y_tr, y_test = train_test_split(
    x, y, train_size = 0.8)
x_val, x_test, y_val, y_test = train_test_split(
    x_test, y_test, train_size = 0.5)


seed = 4321
np.random.seed(seed)
tf.random.set_seed(seed)

scaler = MaxAbsScaler()
x_tr = scaler.fit_transform(x_tr)
x_test = scaler.transform(x_test)
x_val = scaler.transform(x_val)

x_test = np.clip(x_test, 0, 1)
x_val = np.clip(x_val, 0, 1)


pca = PCA(n_components = 10)
xs_tr = pca.fit_transform(x_tr)
xs_test = pca.transform(x_test)
xs_val = pca.transform(x_val)

state_0 = [[1], [0]]
M = state_0 * np.conj(state_0).T


dev = qml.device("default.qubit", wires=nqubits)
qnn = qml.QNode(qnn_circuit, dev, interface="tf")



weights = {"theta": 8}
qlayer = qml.qnn.KerasLayer(qnn, weights, output_dim=1)

model = tf.keras.models.Sequential([qlayer])


opt = tf.keras.optimizers.Adam(learning_rate = 0.005)
model.compile(opt, loss=tf.keras.losses.BinaryCrossentropy(),  metrics=[keras.metrics.BinaryAccuracy()])


earlystop = tf.keras.callbacks.EarlyStopping(
    monitor = "val_loss", patience = 2, verbose = 1,
    restore_best_weights = True)

print (xs_tr.shape)
print (y_tr.shape)

history = model.fit(xs_tr, y_tr, epochs = 50, shuffle = True,
    validation_data = (xs_val, y_val),
    batch_size = 20, 
    callbacks = [earlystop])



import matplotlib.pyplot as plt

def plot_losses(history):
    tr_loss = history.history["loss"]
    val_loss = history.history["val_loss"]
    epochs = np.array(range(len(tr_loss))) + 1
    plt.plot(epochs, tr_loss, label = "Training loss")
    plt.plot(epochs, val_loss, label = "Validation loss")
    plt.xlabel("Epoch")
    plt.legend()
    plt.show()

plot_losses(history)