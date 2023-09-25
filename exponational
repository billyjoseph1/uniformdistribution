# Import necessary libraries
import matplotlib.pyplot as plt
from IPython.display import Math, Latex
from IPython.core.display import Image
from scipy.stats import expon
import seaborn as sns

# Generate random numbers from an exponential distribution
data_expon = expon.rvs(scale=1, loc=0, size=1000)

# Create a seaborn histogram with KDE
ax = sns.distplot(data_expon, kde=True,
                  bins=100,
                  color='skyblue',
                  hist_kws={"linewidth": 15, 'alpha': 1})

# Set labels for the x-axis and y-axis
ax.set(xlabel='Exponential Distribution', ylabel='Frequency')

# Display the plot
plt.show()
