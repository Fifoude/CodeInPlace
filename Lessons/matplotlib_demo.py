import matplotlib.pyplot as plt
import math

def make_a_graph():
    nums = []
    squares = []
    doubles = []

    for i in range (-15, 15):
        nums.append(i)
        squares.append(i * i)
        doubles.append(i * 2)

    plt.plot(nums, squares)
    plt.plot(nums, doubles)
    plt.legend(['y = x^2', 'y = 2x'])
    # plt.show()
    plt.savefig('my_first_graph.png')

make_a_graph()