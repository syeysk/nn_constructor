import matplotlib.pyplot as plt

if __name__ == '__main__':
    f = (0, 2)

    or0 = [[0, 0]]
    or1 = [[0, 1], [1, 0], [1, 1]]

    # plt.scatter([x[0] for x in or0], [y[1] for y in or0], s=2, c='red')
    # plt.scatter([x[0] for x in or1], [y[1] for y in or1], s=2, c='green')
    plt.scatter([x[0] for x in or0], [y[1] for y in or0], s=10, c='red')
    plt.scatter([x[0] for x in or1], [y[1] for y in or1], s=10, c='green')
    plt.plot(f)
    plt.grid(True)
    plt.show()
