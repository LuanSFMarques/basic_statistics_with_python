import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

array1 = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(f"Numpy Array 1: {array1}\n")

array2 = np.arange(0, 101, 10)
print(f"Numpy Array 2: {array2}\n")

array2_mean = array2.mean()
array2_median = np.median(array2)
array2_mode = stats.mode(array2).mode

print(f"Array 2 mean: {array2_mean}")
print(f"Array 2 median: {array2_median}")
print(f"Array 2 mode: {array2_mode}\n") # we need to call ".mode" again in the end of the line because the function .mode() returns a object, inside this object we have what we want, the "mode" as an numpy int.

array3 = np.random.normal(loc=0, scale=2, size=50000)
print(f"Numpy Array 3: {array3}\n")

#counts, bin_edges, _ = plt.hist(array3, bins=9)
#plt.xticks(bin_edges, rotation=45)

plt.hist(array3, bins=200)

array3_mean = np.round((array3.mean()), 4)
array3_median = np.round(np.median(array3), 4)

print(f"Array 3 Mean: {array3_mean}")
print(f"Array 3 Median: {array3_median}\n")

plt.axvline(array3_mean, color='red', linewidth=2, label=f'Mean {array3_mean}')
plt.axvline(array3_mean, color='yellow', linewidth=2, label=f'Median {array3_median}')

plt.gcf().set_size_inches(12, 6)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

plt.show()