"""
Made by www.AZIZBEKDEV.com

data from https://www.statista.com/
"""
from matplotlib import pyplot as plt
import numpy as np

percentage = np.array([
    26.78,
    23.66,
    22.15,
    8.35,
    7.09,
    6.55,
    5.33,
    4.33,
    3.74,
    3.43
])

languages = np.array([
    "Python",
    "JavaScript",
    "Java",
    "C#",
    "PHP",
    "C++",
    "C",
    "R",
    "Swift",
    "Objective C"
])

plt.bar(languages, percentage)

plt.xlabel("Languages")
plt.ylabel("Percentage")
plt.title("The most popular programming languages in 2021 (TIOBE Index)")


if __name__ == "__main__":
    plt.show()