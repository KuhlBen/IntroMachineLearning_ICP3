import numpy as np

# Create a random vector of size 15 with integers in the range 1-20
random_vector = np.random.randint(1, 21, size=15)

# Reshape the array to 3 by 5
reshaped_array = random_vector.reshape(3, 5)

# Print the array shape
print("Shape of the array after reshaping:", reshaped_array.shape)
print(reshaped_array)
print()

# Replace the max in each row by 0
reshaped_array[np.arange(reshaped_array.shape[0]), np.argmax(reshaped_array, axis=1)] = 0

print("Array after replacing max in each row with 0:")
print(reshaped_array)

# Create a 2-dimensional array of size 4x3 with 4-byte integer elements
array_4x3 = np.zeros((4, 3), dtype=np.int32)

# Print the shape, type, and data type of the array
print("\nShape of the 4x3 array:", array_4x3.shape)
print(array_4x3)
print()
print("Type of the array:", type(array_4x3))
print("Data type of the array elements:", array_4x3.dtype)
