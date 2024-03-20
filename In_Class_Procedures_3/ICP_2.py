import numpy as np

# Define the square array
square_array = np.array([[3, -2], [1, 0]])

# Compute eigenvalues and right eigenvectors
eigenvalues, right_eigenvectors = np.linalg.eig(square_array)

# Print the eigenvalues and right eigenvectors
print("Eigenvalues:")
print(eigenvalues)
print("\nRight Eigenvectors:")
print(right_eigenvectors)
