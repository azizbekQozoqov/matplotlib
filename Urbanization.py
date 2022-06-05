"""
Made by www.AZIZBEKDEV.com

data from https://www.statista.com/
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn")

urb_uz = np.array([
    50.96,
    51.15,
    51.05,
    50.95,
    50.85,
    50.75,
    50.65,
    50.55,
    50.48,
    50.43,
    50.42
])

urb_kz = np.array([
    56.83,
    56.9,
    56.97,
    57.05,
    57.12,
    57.19,
    57.26,
    57.34,
    57.43,
    57.54,
    57.67
])

urb_ind = np.array([
    30.93,
    31.28,
    31.63,
    32,
    32.38,
    32.78,
    33.18,
    33.6,
    34.03,
    34.47,
    34.93
])

years = np.array([2010, 2011,2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])

countries = np.array(['Uzbekistan', 'Kazakhstan', 'India'])

plt.plot\
    (years, urb_uz, marker="o", color="#42AD2D")

plt.plot\
    (years, urb_kz, marker="P",color="#2BDEE1", linestyle="-." )

plt.plot\
    (years, urb_ind, marker="X", color="#C21E3F")

# plt.tight_layout()
plt.xlabel("Years")
plt.ylabel("Percentage (%)")
plt.title("Countries urbanization from 2010 to 2020 (by percent)")
plt.legend(countries, loc="center left")

if __name__ == "__main__":
    plt.show()