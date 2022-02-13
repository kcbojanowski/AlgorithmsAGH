from time import time

if __name__ == "__main__":
    start_time = time()
    L = [1, 2, 3, 4, 5]
    resultpython = []
    resultcpp = []

    for i in L:
        resultpython.append(i*i)
    print("1.: ", resultpython)
    time_python = time()-start_time
    print("time by python method: ", time_python)
    for i in range(1, len(L)+1):
        resultcpp.append(i*i)
    print("2.: ", resultcpp)
    time_cpp = time() - start_time - time_python
    print("time by cpp method: ", time_cpp)

    if resultpython == resultcpp:
        print("Results are the same")
    else:
        print("Results are not the same")