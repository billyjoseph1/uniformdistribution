# Import necessary libraries
import matplotlib.pyplot as plt
from IPython.display import Math, Latex
from IPython.core.display import Image
from scipy.stats import poisson
import seaborn as sns

# Generate random numbers from a Poisson distribution
data_poisson = poisson.rvs(mu=3, size=10000, random_state=42)

# Create a seaborn histogram without KDE
ax = sns.distplot(data_poisson, bins=30,
                  kde=False,
                  color='skyblue',
                  hist_kws={"linewidth": 15, 'alpha': 1})

# Set labels for the x-axis and y-axis
ax.set(xlabel='Poisson Distribution', ylabel='Frequency')

# Display the plot
plt.show()
