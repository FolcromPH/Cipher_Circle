from qutip import *
import numpy as np
import math
import urllib.request
import http.client
import time

# Define the quantum state |H_state>
# Uncomment one of the following to test different states:
H_state = (np.sqrt(0.8) * basis(2, 0) + np.sqrt(0.2) * basis(2, 1)).unit()
#H_state = Qobj([[0.7, 0], [0, 0.3]])
#H_state = Qobj([[0.7, 0], [0, 0.5]])
#H_state = (basis(2, 0) - 1j * basis(2, 1)).unit()
#H_state = Qobj([[1, 0], [0, 0]])  # Pure state |0><0|
#H_state = Qobj([[0, 0], [0, 1]])  # Pure state |1><1|

# Extract amplitudes
amp_0 = H_state[0][0]  # Amplitude of |0>
amp_1 = H_state[1][0]  # Amplitude of |1>
amp_0light = math.ceil(abs(amp_0) * 10)  # Use the magnitude of amp_0
amp_1light = math.ceil(abs(amp_1) * 10)  # Use the magnitude of amp_1

# Compute probabilities for |0> and |1>
prob_0 = abs(amp_0)**2  # Probability of |0>
prob_1 = abs(amp_1)**2  # Probability of |1>

# Determine the Bloch vector components
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

# Prepare the data to send
amp_0light_int = amp_0light * 10;
amp_1light_int = amp_1light * 10;
prob_0_int = prob_0 * 100;
prob_1_int = prob_1 * 100;
data_to_send = f"{amp_0light_int},{amp_1light_int},{prob_0_int:.2f},{prob_1_int:.2f}"

# Function to send data to ESP32
base = "http://192.168.242.237/"

def transfer(data1):
    """Send and receive data to/from the ESP32."""
    try:
        url = base + data1  # Append the data to the base URL
        with urllib.request.urlopen(url, timeout=5) as response:
            result = response.read().decode("utf-8")
            print(f"Sent: {data1} | Response: {result}")
            return result
    except http.client.HTTPException as e:
        print(f"HTTP error: {e}")
        return None
    except urllib.error.URLError as e:
        print(f"Connection error: {e}")
        return None

# Send quantum state information (only digits) to ESP32
print("Sending data to ESP32...")
transfer(data_to_send)
from qutip import *
import numpy as np
import math
import urllib.request
import http.client
import time

# Define the quantum state |H_state>
# Uncomment one of the following to test different states:
H_state = (np.sqrt(0.8) * basis(2, 0) + np.sqrt(0.2) * basis(2, 1)).unit()
#H_state = Qobj([[0.7, 0], [0, 0.3]])
#H_state = Qobj([[0.7, 0], [0, 0.5]])
#H_state = (basis(2, 0) - 1j * basis(2, 1)).unit()
#H_state = Qobj([[1, 0], [0, 0]])  # Pure state |0><0|
#H_state = Qobj([[0, 0], [0, 1]])  # Pure state |1><1|

# Extract amplitudes
amp_0 = H_state[0][0]  # Amplitude of |0>
amp_1 = H_state[1][0]  # Amplitude of |1>
amp_0light = math.ceil(abs(amp_0) * 10)  # Use the magnitude of amp_0
amp_1light = math.ceil(abs(amp_1) * 10)  # Use the magnitude of amp_1

# Compute probabilities for |0> and |1>
prob_0 = abs(amp_0)**2  # Probability of |0>
prob_1 = abs(amp_1)**2  # Probability of |1>

# Determine the Bloch vector components
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

# Prepare the data to send
amp_0light_int = amp_0light * 10;
amp_1light_int = amp_1light * 10;
prob_0_int = prob_0 * 100;
prob_1_int = prob_1 * 100;
data_to_send = f"{amp_0light_int},{amp_1light_int},{prob_0_int:.2f},{prob_1_int:.2f}"

# Function to send data to ESP32
base = "http://192.168.242.237/"

def transfer(data1):
    """Send and receive data to/from the ESP82."""
    try:
        url = base + data1  # Append the data to the base URL
        with urllib.request.urlopen(url, timeout=5) as response:
            result = response.read().decode("utf-8")
            print(f"Sent: {data1} | Response: {result}")
            return result
    except http.client.HTTPException as e:
        print(f"HTTP error: {e}")
        return None
    except urllib.error.URLError as e:
        print(f"Connection error: {e}")
        return None

# Send quantum state information (only digits) to ESP32
print("Sending data to ESP82...")
transfer(data_to_send)