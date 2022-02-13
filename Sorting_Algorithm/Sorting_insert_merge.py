import time as t
import random


def insertion_sort(A):
    for i in range(1, len(A)):
        pom = A[i]
        j = i - 1
        while j >= 0 and pom < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = pom


def merge(A, l, m, r):
    side1 = m - l + 1
    side2 = r - m

    L = [0] * side1
    R = [0] * side2

    for i in range(0, side1):
        L[i] = A[l + i]

    for j in range(0, side2):
        R[j] = A[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < side1 and j < side2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i < side1:
        A[k] = L[i]
        i += 1
        k += 1
    while j < side2:
        A[k] = R[j]
        j += 1
        k += 1


def merge_sort(A, n, r):
    if n < r:
        m = (n + (r - 1)) // 2
        merge_sort(A, n, m)
        merge_sort(A, m + 1, r)
        merge(A, n, m, r)


if __name__ == "__main__":
    print("### Sorting ###")
    times_i = []
    times_m = []

    for i in range(150):
        arr_i = [random.randint(1, 100000) for j in range(1000)]
        arr_m = arr_i.copy()

        start_i = t.time()
        insertion_sort(arr_i)
        stop_i = round(t.time() - start_i, 6)
        times_i.append(stop_i)

        start_m = t.time()
        merge_sort(arr_m, 0, len(arr_m) - 1)
        stop_m = round(t.time() - start_m, 6)
        times_m.append(stop_m)

    max_insert = max(times_i)
    max_merge = max(times_m)
    min_insert = min(times_i)
    min_merge = min(times_m)
    avg_insert = round(sum(times_i)/len(times_i),6)
    avg_merge = round(sum(times_m) / len(times_m),6)

    print("Insertion sort\t", "Merge sort")
    print("\tMaximum")
    print(str(max_insert), "\t", str(max_merge))
    print("\tMinimum")
    print(str(min_insert), "\t", str(min_merge))
    print("\tAverage")
    print(str(avg_insert), "\t", str(avg_merge))
    print("\t--------")