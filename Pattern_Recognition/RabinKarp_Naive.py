from time import time
import matplotlib.pyplot as plt


def naive_search(txt, pattern):
    n = len(txt[0])
    m = len(pattern[0])
    cords = []
    for i in range(n - m):
        for j in range(n - m):
            if pattern[0] == txt[i][j:j + 3] and pattern[1] == txt[i + 1][j] and pattern[2] == txt[i + 2][j]:
                cords.append((i, j))
    return cords


def rabin_karp(txt, pattern, d, q):
    n = len(txt[0])
    m = len(pattern)
    h = d ** (m - 1) % q
    p = 0
    t_z = 0
    cords = []
    for i in range(1, m):
        p = (d * p + int(pattern[i], 16)) % q
        t_z = (d * t_z + int(txt[0][i], 16)) % q

    for j in range(n - m):
        for k in range(n - m):
            if p == t_z:
                if pattern == txt[j][k:k + m] and pattern[1] == txt[j + 1][k] \
                        and pattern[2] == txt[j + 2][k]:
                    cords.append((j, k))
            if k < n - m:
                t_z = (d * (t_z - int(txt[j][k + 1], 16) * h) + int(txt[j][k + m], 16)) % q
    return cords


if __name__ == "__main__":
    # pattern
    P_1 = ['ABC', 'B', 'C']
    P_2 = 'ABC'
    times_n = []
    times_r = []
    matrix = [1000, 2000, 3000, 4000, 5000, 8000]
    nr_of_elems = []

    for i in matrix:
        file = open(str(i) + "_pattern.txt")
        text = []
        for line in file:
            text.append(line.strip())
        start_n = time()
        naive_cords = naive_search(text, P_1)
        time_n = time() - start_n
        start_r = time()
        rabin_cords = rabin_karp(text, P_2, 10, 10)
        time_r = time() - start_r
        times_n.append(time_n)
        times_r.append(time_r)
        nr_of_elems.append(i*i)
        print("-" * 100)
        print("\t # TIMES #")
        print("For N = {} \ntime for naive search is {} s \ntime for Rabin-Karp search is {} s"
              .format(i, round(time_n, 5), round(time_r, 5)))
        print("\t # NUMBER OF INCREMENTS #")
        print("Number of increments for naive search is {} and for Rabin-Karp search is {}"
              .format(len(naive_cords), len(rabin_cords)))
        print("\t # CORDS #")
        print("cords of pattern (naive) :", naive_cords)
        print("cords of pattern (Rabin-Karp) :", rabin_cords)

    plt.plot(nr_of_elems, times_n, 'og', label='Naive Algorithm')
    plt.plot(nr_of_elems, times_r, 'ob', label='Rabin-Karp Algorithm')
    plt.ylabel('Time [ns]')
    plt.xlabel('Amount of elements in matrix')
    plt.title('Time dependence on a amount of elements')
    plt.legend()
    plt.show()
