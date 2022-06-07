"""
Very basic scatter plot example
"""

import numpy as np
import matplotlib.pyplot as plt

plt.xkcd()

x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)

# x1 = np.array()

plt.scatter(x+0.1, y+0.13, s=10, c="green", alpha=0.5)
plt.scatter(x+1, y+2, s=4, marker="x", c="red", linewidth=1, alpha=0.4)

plt.tight_layout()
plt.title("Very basic scatter plot example")

if __name__ == "__main__":
    plt.show()