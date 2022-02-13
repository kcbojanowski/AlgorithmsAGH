from time import *


def Duplicates(L):
    Repeated = []
    for number in L:
        if L.count(number) > 1:
            Repeated.append(i)
    Repeated.sort()
    return Repeated


if __name__ == "__main__":
    start_time = time()
    L = [1, 2]
    for i in range(2, 48):
        pom = (L[i-2] + L[i-1]) / (L[i-1] - L[i-2])
        L.append(pom)

    print(L)
    L.sort()
    av_of_L = sum(L)/len(L)
    median_of_L = (L[23] + L[24])/2
    print("avarage of L is: ", av_of_L)
    print("median of L is: ", median_of_L)
    print("Repeated: ", Duplicates(L))
    if not Duplicates(L):
        print("No Duplicates")
    print("Time: ", time() - start_time)
