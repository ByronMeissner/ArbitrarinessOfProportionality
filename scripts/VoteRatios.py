!pip install seaborn
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Use a seaborn style for better aesthetics
sns.set(style="whitegrid")

# Parameters for the normal distributions
mean1 = 0.3
std_dev1 = 0.05
mean2 = 0.7
std_dev2 = 0.1
n_items = 16000

# Generate data for the normal distributions
data1 = np.random.normal(mean1, std_dev1, n_items // 2)
data2 = np.random.normal(mean2, std_dev2, n_items // 2)

# Concatenate the data
data = np.concatenate([data1, data2])

# Create the histogram
plt.figure(figsize=(14, 7))
plt.hist(data, bins=100, range=(0, 1), alpha=0.7, color='gray', edgecolor='black')

# Plot individual distributions for clarity
x = np.linspace(0, 1, 1000)
y1 = (1 / (np.sqrt(2 * np.pi) * std_dev1)) * np.exp(-0.5 * ((x - mean1) / std_dev1) ** 2)
y2 = (1 / (np.sqrt(2 * np.pi) * std_dev2)) * np.exp(-0.5 * ((x - mean2) / std_dev2) ** 2)

# Scale the y-values to match the histogram
y1 = y1 * (n_items / 2) * (1 / (np.sum(y1) * (x[1] - x[0])))
y2 = y2 * (n_items / 2) * (1 / (np.sum(y2) * (x[1] - x[0])))

plt.plot(x, y1, color='blue', linewidth=2, label='PPP-NotApplied')
plt.fill_between(x, y1, color='blue', alpha=0.3)
plt.plot(x, y2, color='red', linewidth=2, label='PPP-Applied')
plt.fill_between(x, y2, color='red', alpha=0.3)

# Add titles and labels
plt.title('Vote Ratios', fontsize=18)
plt.xlabel('Vote Ratios of Judges', fontsize=14)
plt.ylabel('Number of Court Rulings', fontsize=14)
plt.legend(fontsize=12)

# Improve the overall appearance
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()