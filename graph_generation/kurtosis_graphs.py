import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Base normal distribution
np.random.seed(42)  # Ensuring reproducibility
data = np.random.normal(loc=0, scale=1, size=50000)

# Create a distribution with positive kurtosis (leptokurtic) - heavier tails
data_pos_kurt = np.concatenate([data, np.random.normal(loc=0, scale=0.5, size=25000)])  # Add more values near mean

# Create a distribution with negative kurtosis (platykurtic) - lighter tails
data_neg_kurt = (np.random.beta(a=2, b=2, size=50000) - 0.5)

# Calculate kurtosis
print("Kurtosis (Base Normal):", stats.kurtosis(data, fisher=True))
print("Kurtosis (Positive):", stats.kurtosis(data_pos_kurt, fisher=True))
print("Kurtosis (Negative):", stats.kurtosis(data_neg_kurt, fisher=True))

fig, axes = plt.subplots(1, 3, figsize=(12, 4))
fig.suptitle("Negative Kurtosis X Mesokurtic X Positive Kurtosis")
axes[2].hist(data_pos_kurt,color="#00618c", bins=500)
axes[1].hist(data, color="black", bins=500)
axes[0].hist(data_neg_kurt,color="#8c0000", bins=500)

plt.show()