# beginner_numpy_demo.py
# A simple NumPy demo program for beginners
  
import numpy as np
    
# 1. Create a 1D array
arr1 = np.array([1, 2, 3, 4, 5])    
print("1D Array:", arr1)
  
# 2. Create a 2D array (matrix)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr2)

# 3. Generate arrays using NumPy functions
zeros = np.zeros((3, 3))   # 3x3 array of zeros
ones = np.ones((2, 2))     # 2x2 array of ones
rand = np.random.rand(3, 3)  # Random numbers

print("\nZeros Array:\n", zeros)
print("\nOnes Array:\n", ones)
print("\nRandom Array:\n", rand)

# 4. Basic operations
print("\nArray Addition:", arr1 + 10)
print("Array Multiplication:", arr1 * 2)

# 5. Slicing and indexing
print("\nFirst element:", arr1[0])
print("Last two elements:", arr1[-2:])

# 6. Useful functions
print("\nMean:", np.mean(arr1))
print("Max:", np.max(arr1))
print("Reshaped 2D array:\n", arr1.reshape(5, 1))
