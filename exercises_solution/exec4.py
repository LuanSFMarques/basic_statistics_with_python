import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

array = np.random.normal(loc=100, scale=4, size=50000) # Symmetric

plt.figure(figsize=(14,6))
plt.hist(array, bins=1000)

plt.xlabel("Values", fontsize=12, fontweight='bold')
plt.ylabel("Frequency", fontsize=12, fontweight='bold')

plt.show()

# Solution: The mean is equal to the median.
# Why: The graph appears symmetrical, so the mean and the median should be very similar in value.