import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

array4 = stats.skewnorm.rvs(a=3, loc=0, scale=2, size=50000)
mode_adjustment = np.percentile(array4, 50)  # Approximate mode using the median
array4 -= mode_adjustment  # Shift distribution so mode aligns with 0

#newar = stats.skewnorm.rvs(a=-10, loc=30, scale=2, size=5000)
#array4 = np.append(array4, newar)

array4_mean = np.round(array4.mean(), 4)
array4_median = np.round(np.median(array4), 4)

plt.figure(figsize=(14,8))
plt.hist(array4, bins=200)

plt.axvline(array4_mean, color='red', linewidth=2, label=f"Mean: {array4_mean}")
plt.axvline(array4_median, color='Chartreuse', linewidth=2, label=f"Median: {array4_median}")

plt.xlabel('Values')
plt.ylabel('Frequency')

plt.legend()

plt.show()