if __name__ == "__main__":
    lst = []
    lstxx = []

    for i in range(504,3000,7):
        lst.append(i)

    for element in lst:
        if element % 5 == 0:
            lst.remove(element)
        else:
            pass
    lststring = ''.join(map(str, lst))

    print("1) ", lst)
    print("2) ", lststring)

    for i in lststring:
        lstxx = lststring.replace('21','XX')

    counter = lstxx.count('XX')
    print("3) ", lstxx)
    print("number of XX is: ", counter)

