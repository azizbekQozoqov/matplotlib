from secrets import token_urlsafe
from matplotlib import pyplot as plt

plt.plot([10, 20], [1, 3], label="Akola PNG")


plt.legend()
plt.title("Yeap")
plt.xlabel("Akola")
plt.ylabel("PNG")

if __name__ == "__main__":
    plt.savefig(f"./figs/{token_urlsafe(17)}.png")
    plt.show()