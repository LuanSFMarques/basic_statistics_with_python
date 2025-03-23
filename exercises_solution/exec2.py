import numpy as np

array = np.array([5, 10, 15, 25, 50, 70, 100, 200])
mean = np.mean(array)
median = np.median(array)

print(f"Mean: {mean}, Median: {median}")

# Solution: Mean: 59.375, Median: 37.5
# Graph: Asymmetrical (59.3 is quite distant from 37.5)