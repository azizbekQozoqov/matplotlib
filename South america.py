"""
Made by www.AZIZBEKDEV.com

data from https://www.wikipedia.org/
"""
import numpy as np
from matplotlib import pyplot as plt


slices = np.array([
    8_515_767, 
    2_780_400, 
    1_285_216, 
    1_141_748, 
    1_098_581, 
    916_445,
    756_096,
    406_752,
    276_841,
    214_969,
    176_215,
    163_820
])
labels = np.array([
    'Brazil', 
    'Argentina', 
    'Peru',
    'Colombia',
    'Bolivia',
    'Venezuela',
    'Chile',
    'Paraguay',
    'Ecuador',
    'Guyana',
    'Uruguay',
    'Suriname'

])


colors = np.array(['#F4CE12', "#6CF1D9", "#F72F2F", "#E0BF17", "#1A9110", "#102F9B", "#FF0808", "#A3CBD2", "#363A6E", "#38BF20", "#ACBCDE", "#217512"])
explode = np.array([0 , 0.1, 0, 0, 0.1, 0, 0, 0, 0.1, 0 ,0, 0.2])

plt.pie\
(
    slices,
    labels=labels,
    autopct="%1.1f%%",
    explode=explode,
    colors=colors
)


plt.tight_layout()

if __name__ == "__main__":
    plt.show()