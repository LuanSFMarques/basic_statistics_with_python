import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

array = stats.skewnorm.rvs(a=-5, loc=100, scale=2, size=50000) # Skew to the left

plt.figure(figsize=(14,6))
plt.hist(array, bins=1000)

plt.xlabel("Values", fontsize=12, fontweight='bold')
plt.ylabel("Frequency", fontsize=12, fontweight='bold')

plt.show()