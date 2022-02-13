from array import *
from time import *


def duplicates(L):
    repeated = []
    for number in L:
        if L.count(number) > 1:
            repeated.append(number)
    return repeated


def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == "__main__":
    start_time = time()
    L = array('f', [1, 2])
    for i in range(2, 48):
        pom = (L[i-2] + L[i-1]) / (L[i-1] - L[i-2])
        L.append(pom)

    print(L)
    bubbleSort(L)
    av_of_L = sum(L)/len(L)
    median_of_L = (L[23] + L[24])/2
    print("avarage of L is: ", av_of_L)
    print("median of L is: ", median_of_L)
    print("Repeated: ", duplicates(L))
    if not duplicates(L):
        print("No Duplicates")
    Czas = time() - start_time
    print("Time: ", Czas, "s")
