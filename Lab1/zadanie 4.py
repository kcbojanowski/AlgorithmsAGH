if __name__ == "__main__":

    L = [1, 2, 3]
    try:
            print(L[4])
    except IndexError:
        print("Wrong Index")

    try:
        for j in range(len(L)+1):
            print(L[j+2] // (L[j+1] - L[j+1]))
    except ZeroDivisionError:
        print("Divided by 0")

    try:
       sqrt(L[1])
    except NameError:
        print("No function")

