import random
import math


def function(x):
    return math.sin(x)


if __name__ == "__main__":

    # interface
    print('range of integration (max is pi) : ')
    a = float(input('from: '))
    b = float(input('to: '))
    n = int(input('amount of points: '))
    random_x = []
    random_y = []
    counter = 0

    for i in range(n):      # adding random number to x and y
        x = random.uniform(a, b)
        random_x.append(x)
        y = random.uniform(0, 1)
        random_y.append(y)

    points = [list(i) for i in zip(random_x, random_y)]     # connecting x and y int list of lists

    for cords in points:
        if cords[1] <= function(cords[0]):      # searching for points that are result of function
            counter += 1

    ratio = counter / n
    result = ratio * (b-a)
    print('result: ', result)       # printing result
