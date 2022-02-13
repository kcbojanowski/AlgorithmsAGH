from random import uniform
from time import perf_counter_ns
import matplotlib.pyplot as plt


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.add(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.add(value)

    def maximum(self, n=0):
        if n == 0:
            return self.right.maximum() if self.right else self.value
        else:
            return self.left.maximum() if self.value else self.right

    def minimum(self, n=0):
        if n == 0:
            return self.left.minimum() if self.left else self.value
        else:
            return self.right.minimum() if self.value else self.left

    def search(self, value):
        if self.value == value:
            return True
        elif value < self.value:
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            return self.right.search(value) if self.right else False

    def __str__(self, position=''):
        string = position + str(self.value)
        number = ' ' * len(string) + '-' * (position.count('-') + 1)
        if self.left and self.right:
            string += '' + self.left.__str__(number.strip())
            string += '\n' + self.right.__str__(number)
        elif self.left:
            string += '' + self.left.__str__(number.strip())
        elif self.right:
            string += '' + self.right.__str__(number.strip())
        return string


class BinaryTree:
    def __init__(self):
        self.data = {}

    def __str__(self):
        string = "\n".join([i.__str__() for i in self.data.values()])
        return string

    def add(self, value):
        root = int(value) + 0.5
        if root not in self.data:
            self.data[root] = Node(root)
        self.data[root].add(value)

    def search(self, value):
        root = int(value) + 0.5
        if value == root:
            return False
        else:
            if root in self.data:
                return self.data[root].search(value)
            else:
                return False

    def maximum(self, y):
        y = int(y) + 0.5
        if y in self.data:
            temp = self.data[y].maximum()
            if temp == y:
                return self.data[y].maximum(1)
            else:
                return temp
        else:
            return False

    def minimum(self, y):
        y = int(y) + 0.5
        if y in self.data:
            temp = self.data[y].minimum()
            if temp == y:
                return self.data[y].minimum(1)
            else:
                return temp
        else:
            return False


def tree_build(t, value):
    for i in value:
        t.add(i)
    return t


if __name__ == "__main__":
    time_insert = []
    time_min = []
    time_max = []
    time_search = []
    data = [round(uniform(0, 10), 2) for i in range(1000)]
    Nr_of_elems = [25, 50, 100, 500, 1000]

    ex_data = [1.3, 1.6, 3.7, 4.0, 4.99, 7.3, 7.8, 7.7, 7.9, 7.6, 9.3]
    ex_struct = BinaryTree()
    tree_build(ex_struct, ex_data)
    print(ex_struct)

    for elem in Nr_of_elems:
        t = BinaryTree()
        tree = tree_build(t, data)
        temp_add = []
        temp_min = []
        temp_max = []
        temp_s = []

        for i in range(0, 1000):
            temp = round(uniform(0, 10), 2)
            temp_2 = round(uniform(0, 10), 2)

            start_add = perf_counter_ns()
            tree.add(temp)
            stop_add = perf_counter_ns() - start_add

            start_min = perf_counter_ns()
            tree.minimum(temp_2)
            stop_min = perf_counter_ns() - start_min

            start_max = perf_counter_ns()
            tree.maximum(temp_2)
            stop_max = perf_counter_ns() - start_max

            start_s = perf_counter_ns()
            tree.search(temp)
            stop_s = perf_counter_ns() - start_s

            temp_add.append(stop_add)
            temp_min.append(stop_min)
            temp_max.append(stop_max)
            temp_s.append(stop_s)

        time_insert.append(sum(temp_add) / len(temp_add))
        time_min.append(sum(temp_min) / len(temp_min))
        time_max.append(sum(temp_max) / len(temp_max))
        time_search.append(sum(temp_s) / len(temp_s))

    for i in range(len(Nr_of_elems)):
        print('Average time of adding for {} elements: {} ns '.format(Nr_of_elems[i], time_insert[i],))
        print('Average time of minimum for {} elements: {} ns'.format(Nr_of_elems[i], time_min[i]))
        print('Average time of maximum for {} elements: {} ns'.format(Nr_of_elems[i], time_max[i]))
        print('Average time of search for {} elements: {} ns'.format(Nr_of_elems[i], time_search[i]))
        print(50 * '-')

    plt.plot(Nr_of_elems, time_min, 'or', label='Average time of minimum')
    plt.plot(Nr_of_elems, time_max, 'ob', label='Average time of maximum')
    plt.plot(Nr_of_elems, time_insert, 'og', label='Average time of add')
    plt.plot(Nr_of_elems, time_search, 'om', label='Average time of search')
    plt.ylabel('Time [ns]')
    plt.xlabel('Number of elements')
    plt.title('Time dependence on number of elements')
    plt.legend()
    plt.show()

