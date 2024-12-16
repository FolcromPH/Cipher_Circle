from qutip import *
import numpy as np
import matplotlib.pyplot as plt
import math

# Define the quantum state |H_state>
# Uncomment one of the following to test different states:
H_state = (np.sqrt(0.8) * basis(2, 0) + np.sqrt(0.2) * basis(2, 1)).unit()
#H_state = Qobj([[0.7, 0], [0, 0.3]])
#H_state = Qobj([[0.7, 0], [0, 0.5]])
#H_state = (basis(2, 0) - 1j * basis(2, 1)).unit()

# Extract amplitudes
amp_0 = H_state[0][0]  # Amplitude of |0>
amp_1 = H_state[1][0]  # Amplitude of |1>
amp_0light = math.ceil(abs(amp_0) * 10) # Use the magnitude of amp_0
amp_1light = math.ceil(abs(amp_1) * 10)# Use the magnitude of amp_1

# Compute probabilities for |0> and |1>
prob_0 = abs(amp_0)**2  # Probability of |0>
prob_1 = abs(amp_1)**2  # Probability of |1>

# Determine the Bloch vector
bloch_vector = [
    np.real(amp_0 * np.conj(amp_1)),  # x component
    np.imag(amp_0 * np.conj(amp_1)),  # y component
    prob_0 - prob_1                   # z component
]

# Map Bloch vector to faces
if abs(bloch_vector[2]) > abs(bloch_vector[0]) and abs(bloch_vector[2]) > abs(bloch_vector[1]):
    near_face = "z-axis face"
elif abs(bloch_vector[0]) > abs(bloch_vector[1]) and abs(bloch_vector[0]) > abs(bloch_vector[2]):
    near_face = "x-axis face"
else:
    near_face = "y-axis face"

# Print amplitudes, probabilities, and face information
print(f"Amplitude of |0>: {amp_0light}")
print(f"Amplitude of |1>: {amp_1light}")
print(f"Probability in |0>: {prob_0:.2f}")
print(f"Probability in |1>: {prob_1:.2f}")
print(f"The state is near the {near_face}.")

# Visualize on the Bloch sphere
b = Bloch()
b.add_states(H_state)
b.show()
plt.show()
