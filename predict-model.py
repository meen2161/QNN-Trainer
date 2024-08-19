import pennylane as qml
import tensorflow as tf
import numpy as np

# Redefine the QNode and device
nqubits = 4

def ZZFeatureMap(nqubits, data):
    nload = min(len(data), nqubits)
    for i in range(nload):
        qml.Hadamard(i)
        qml.RZ(2.0 * data[:, i], wires=i)
    for pair in list(combinations(range(nload), 2)):
        q0 = pair[0]
        q1 = pair[1]
        qml.CZ(wires=[q0, q1])
        qml.RZ(2.0 * (np.pi - data[:, q0]) * (np.pi - data[:, q1]), wires=q1)
        qml.CZ(wires=[q0, q1])

def TwoLocal(nqubits, theta, reps=1):
    for r in range(reps):
        for i in range(nqubits):
            qml.RY(theta[r * nqubits + i], wires=i)
        for i in range(nqubits - 1):
            qml.CNOT(wires=[i, i + 1])
    for i in range(nqubits):
        qml.RY(theta[reps * nqubits + i], wires=i)

def qnn_circuit(inputs, theta):
    global nqubits
    ZZFeatureMap(nqubits, inputs)
    TwoLocal(nqubits=nqubits, theta=theta, reps=1)
    return qml.expval(qml.Hermitian(M, wires=[0]))

state_0 = [[1], [0]]
M = state_0 * np.conj(state_0).T

dev = qml.device("default.qubit", wires=nqubits)
qnn = qml.QNode(qnn_circuit, dev, interface="tf")

# Load the model
loaded_model = tf.keras.models.load_model('qnn.h5', custom_objects={'KerasLayer': lambda *args, **kwargs: qml.qnn.KerasLayer(qnn, *args, **kwargs)})
print("Model loaded from 'qnn.h5'")



from sklearn.decomposition import PCA
from itertools import combinations

# Sample input with 4 features
sample_input = np.array([[10, 1, 4, 3]])


# Make prediction
prediction = loaded_model.predict(sample_input)
print("Prediction:", prediction)