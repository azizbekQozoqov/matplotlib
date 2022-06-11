import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-whitegrid")

users = np.array([
    5.43,
    7.01,
    8.09,
    10.09,
    13.3,
    14.8,
    16.9,
    18.1,
    23.4,
    23.7,
    24.0
])

years = np.arange(start=2012, stop=2023)


plt.barh(years, users, color="#a862ea")


plt.title("Internet users in UZBEKISTAN (2012 - 2022)")
plt.ylabel("Years")
plt.xlabel("Users (million)")


if __name__ == "__main__":
    plt.show()