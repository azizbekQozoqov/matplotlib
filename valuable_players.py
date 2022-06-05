"""
Made by www.AZIZBEKDEV.com

data from https://www.transfermarkt.com/
"""
import matplotlib.pyplot as plt
import numpy as np

plt.xkcd()

values = np.array([
    160,
    150,
    100,
    100,
    100,
    90,
    90,
    90,
    85,
    85
])

players = np.array([
    "Kylian Mbappé",
    "Erling Haaland",
    "Vinicius Junior",
    "Mohamed Salah",
    "Harry Kane",
    "Phil Foden",
    "Bruno Fernandes",
    "Kevin De Bruyne",
    "Dušan Vlahović",
    "Joshua Kimmich"
])

plt.barh(players, values, color="r")

plt.title("MOST VALUABLE FOOTBALL PLAYERS")
plt.tight_layout()
plt.xlabel("Value (m/€)")
plt.ylabel("Players")

plt.show()