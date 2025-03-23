import numpy as np

array = np.array([1, 3, 4, 4, 5, 7, 8, 9, 9, 10, 12, 13, 14, 15, 16])
mean = np.mean(array)
median = np.median(array)

print(f"Mean: {mean}, Median: {median}")

# Solution: Mean: 8.666666666666666, Median: 9.0
# Graph: Almost assymetrical (8.6 is quite close to 9)