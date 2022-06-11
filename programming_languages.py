"""
Made by www.AZIZBEKDEV.com

data from https://www.statista.com/
"""
from matplotlib import pyplot as plt
import numpy as np

# print(plt.style.available)
plt.style.use("ggplot")

percentage = np.array([
    3.43,
    3.74,
    4.33,
    5.33,
    6.55,
    7.09,
    8.35,
    22.15,
    23.66,
    26.78,
    
])

languages = np.array([
    "Objective C",
    "Swift",
    "R",
    "C",
    "C++",
    "PHP",
    "C#",
    "Java",
    "JavaScript",
    "Python",
])

plt.barh(languages, percentage, color='#2cd69a')

plt.title("The most popular programming languages in 2021 (TIOBE Index)")
plt.xlabel("Percentage (%)")
plt.ylabel("Languages")


if __name__ == "__main__":
    plt.show()