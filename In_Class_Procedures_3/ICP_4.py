import numpy as np

# Original 3x2 array
original_array_3x2 = np.array([[1, 2], [3, 4], [5, 6]])

# Reshape to 2x3 without changing data
reshaped_array_2x3 = original_array_3x2.reshape(2, 3)

# Print the original and reshaped arrays
print("Original 3x2 array:")
print(original_array_3x2)
print("\nReshaped 2x3 array without changing data:")
print(reshaped_array_2x3)
