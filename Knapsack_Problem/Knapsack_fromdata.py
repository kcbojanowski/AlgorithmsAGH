import numpy as np
import matplotlib.pyplot as plt
from time import time


def packing(x, y, backpack_, height, width, item):
    value = 0
    for i in range(height):
        for j in range(width):
            if ((height + x) <= len(backpack_)) and ((width + y) <= len(backpack_)):
                backpack_[i + x][j + y] = item[0]
                value = item[3]
    return backpack_, value


def select(backpack_, size_, width, height, item):
    temp = False
    value_ = 0
    for i in range(size_ - width + 1):
        for j in range(size_ - height + 1):
            if sum(backpack_[i][j: j + height - 1]) == 0:
                for k in range(width):
                    if backpack_[i + k][j] != 0 or backpack_[i + k][j + height - 1] != 0:
                        temp = False
                        break
                    else:
                        temp = True
                if temp:
                    backpack_, value_ = packing(i, j, backpack_, width, height, item)
                    break
        if temp:
            break

    return temp, backpack_, value_


def pack(backpack_, size_, item):
    width = item[1]
    height = item[2]
    temp, backpack_, value = select(backpack_, size_, width, height, item)
    if not temp:
        width = item[2]
        height = item[1]
        temp, backpack_, value = select(backpack_, size_, width, height, item)

    return backpack_, value


def read_data(path_):
    data = []
    items = open(path_, "r")
    lines = items.readlines()[2:]
    [data.append(list(map(int, line.strip().split(",")))) for line in lines]
    for elem in data:
        elem.append(elem[3] / (elem[1] * elem[2]))
    return data


def visualization(size_, knapsack, flag):
    fig, ax = plt.subplots()
    ax.imshow(knapsack, origin='upper', cmap=plt.get_cmap('gist_ncar'))
    if flag == 1:
        for i in range(size_):
            for j in range(size_):
                c = knapsack[j][i]
                ax.text(i, j, str(int(c)), va='center', ha='center')
    plt.title(f"{size_}x{size_}")
    plt.show()
    plt.savefig(f"knapsack{size_}x{size_}")

def initialization(eq):
    backpack = np.zeros((size, size))
    backpack_value = 0
    for elem in eq:
        backpack, val = pack(backpack, size, elem)
        backpack_value += val
    knapsack = backpack[::-1]
    return np.array(knapsack).astype(int), backpack_value


if __name__ == '__main__':
    # Reading data from three txt files
    paths = ["packages20.txt", "packages100.txt", "packages500.txt"]
    for path in paths:
        print("-" * 50)
        size = int(path[:-4].replace("packages", ""))
        items = read_data(path)
        backpack = np.zeros((size, size))
        backpack_value = 0

        # Greedy Algorithm
        start_greedy = time()
        items.sort(reverse=True, key=lambda items: items[4])
        knapsack, final_value = initialization(items)
        stop_greedy = time() - start_greedy
        print("\t|GREEDY ALGORITHM|")
        print(f"Result for knapsack size {size}x{size} is {final_value}")
        print(f"Time of Iteration is {stop_greedy}s")
        if size == 20:
            visualization(size, knapsack, 1)
        else:
            visualization(size, knapsack, 0)

        # Naive Algorithm
        start_naive = time()
        items.sort(reverse=True, key=lambda items: items[3])
        knapsack, final_value = initialization(items)
        stop_naive = time() - start_naive
        print("\t|NAIVE ALGORITHM|")

        print(f"Result for knapsack size {size}x{size} is {final_value} ")
        print(f"Time of Iteration is {stop_naive}s")
        if size == 20:
            visualization(size, knapsack, 1)
        else:
            visualization(size, knapsack, 0)


