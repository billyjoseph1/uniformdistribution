# Import necessary libraries
import matplotlib.pyplot as plt
from IPython.display import Math, Latex
from IPython.core.display import Image
from scipy.stats import norm
import seaborn as sns

# Set seaborn plotting style and figure size
sns.set(rc={'figure.figsize': (5, 5)})

# Generate random numbers from N(0, 1)
data_normal = norm.rvs(size=10000, loc=0, scale=1)

# Create a seaborn histogram with KDE
ax = sns.distplot(data_normal,
                  bins=100,
                  kde=True,
                  color='skyblue',
                  hist_kws={"linewidth": 15, 'alpha': 1})

# Set labels for the x-axis and y-axis
ax.set(xlabel='Normal Distribution', ylabel='Frequency')

# Display the plot
plt.show()
