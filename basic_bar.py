from matplotlib import pyplot as plt
import numpy as np


# X values - ages
developers_x = np.arange(start=25, stop=36)#[25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# Spliter width
width=0.25

# Y values - salary
py_devs = np.array([35_500, 37_000, 40_000, 45_000, 50_000, 52_000, 55_500, 56_000, 59_000, 62_300, 63_000])
js_devs = np.array([28_000, 35_500, 37_000, 40_000, 45_000, 47_000, 52_000, 53_500, 55_000, 57_000, 61_000])

cpp = np.array([30_000, 32_500, 36_000, 39_000, 45_000, 47_000, 49_000, 53_500, 59_000, 60_000, 62_000])

# Create plots
plt.bar(developers_x - width, py_devs, width=width, color="b")
plt.bar(developers_x, js_devs, width=width, color="y")
plt.bar(developers_x+width, cpp, width=width, color="r")


# Labels
plt.xlabel("Ages")
plt.ylabel("Salary")
plt.title("Developers Salary by ages")
plt.xticks(ticks=developers_x, labels=developers_x)

if __name__ == "__main__":
    plt.show()