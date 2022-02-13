from time import *


if __name__ == "__main__":

    while True:
        text = input("Wprowadz wyraz: ")
        counter = 0
        count = 0
        for words in text:
            if words == " ":
                counter += 1
        if counter != 0:
            text = input("wprowadz tylko jeden wyraz! Ponowna próba: ")
            break
        else:
            break

    # lower case
    word = text.lower()
    # measuring time
    start_time = time()

    # opening SJP
    with open("SJP.txt", "r", encoding="utf8") as polish:
        reader = " "
        while reader:
            reader = polish.readline()
            splitter = reader.split()
            for line in splitter:
                if line == word:
                    count += 1
                    times = time() - start_time
                    print("slowo " + word + " istnieje w j.polskim")
                    print("czas wyszukiwania: ", times, "s")
        if count == 0:
            print("Slowo nie wystepuje w SJP")

        # closing file
        polish.close()
