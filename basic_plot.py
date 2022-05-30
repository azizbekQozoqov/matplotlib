"""
Basic matplotlib

    * Install matplotlib - pip install matplotlib (if you're using ubuntu run this additional command - sudo apt-get install python-tk)

Let's create a program that shows salary of developers by age.

"""

from matplotlib import pyplot as plt
import tkinter.messagebox as mb

# Use default style
# plt.style.use("fivethirtyeight")

plt.xkcd()

# X values - ages
developers_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 45]

# Y values - salary
py_devs = [35_500, 37_000, 40_000, 45_000, 50_000, 52_000, 55_500, 56_000, 59_000, 62_300, 63_000]
js_devs = [28_000, 35_500, 37_000, 40_000, 45_000, 47_000, 52_000, 53_500, 55_000, 57_000, 64_000]

# Create plots
plt.plot(developers_x, py_devs, marker="o", markersize=6,linewidth=3, linestyle="--", color="b", label="Python developers")
plt.plot(developers_x, js_devs, label="JavaScript developers", marker="*", markersize=6, linewidth=3, linestyle="--", color="y")

# plt.grid(True) # Grid style
plt.legend()
plt.xlabel("Ages")
plt.ylabel("Salary")
plt.title("Developers Salary by ages")

if __name__ == "__main__":
    answer = mb.askyesno("Notice", "Let's create a program that shows salary of developers by age.")
    if answer:
        plt.show()