import matplotlib.pyplot as plt
import numpy as np

# Example data for plotting
lambdas = [1100, 1200, 1250, 1300,  1400]
means = [28, 25.2, 23.5, 23, 21]
errors = [3.8, 2.8, 3.4, 3.5, 3.5]

# Plotting the data
plt.figure(figsize=(6, 4))
plt.errorbar(lambdas, means, yerr=errors, fmt='o', color='blue', ecolor='blue', capsize=5)

# Adding a red horizontal line at y=20
plt.axhline(y=20, color='red', linewidth=2)

# Setting the limits for the y-axis
plt.ylim(17, 32)

# Adding titles and labels with specific font sizes
plt.title('Wykres dla lambda z przedziałami ufności', fontsize=12)
plt.xlabel('Oś X', fontsize=10)
plt.ylabel('Oś Y', fontsize=10)

# Adding grid lines
plt.grid(True)

# Displaying the plot
plt.show()
