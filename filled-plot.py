# Import requirements
import pandas as pd
import zedmath as zd
import matplotlib.pyplot as plt

csv_data = pd.read_csv("csv/data-1.csv")
cd_ages = csv_data["Age"]
dev_salaries = csv_data["All_Devs"]
py_salaries = csv_data["Python"]
js_salaries = csv_data["JavaScript"]

plt.plot(
    cd_ages,
    dev_salaries,
    color="#444",
    linestyle="--",
    label="All Developers"
)

plt.plot(
    cd_ages,
    py_salaries,
    color="#000",
    linestyle="--",
    label="All Developers"
)

# Fill
overall_median=53000
plt.fill_between(cd_ages, py_salaries,color="b", alpha=.3, y2=overall_median)


# Title configuration
plt.legend()
plt.title("Median salary (USD) by age")
plt.xlabel("Ages")
plt.ylabel("Median salary (USD)")

# Run file
if __name__ == "__main__":
    plt.show()