from time import *


def hanoi_rec(n, sour, dest, buff):
    if n == 1:
        print(sour + " -> " + dest)
        return None
    hanoi_rec(n - 1, sour, buff, dest)
    print(sour + " -> " + dest)
    hanoi_rec(n - 1, buff, dest, sour)
    return None


def make_move(sour, dest):
    if len(dest) > 0 and len(sour) > 0:
        if int(sour[-1]) < int(dest[-1]):
            dest.append(sour.pop())
        else:
            sour.append(dest.pop())
    elif len(sour) > 0:
        dest.append(sour.pop())

    elif len(dest) > 0:
        sour.append(dest.pop())


def hanoi_ite(n):
    sour = [i + 1 for i in range(n)][::-1]
    buff = []
    dest = []
    if n % 2 == 1:
        for i in range(1, 2 ** n):

            if i % 3 == 1:
                if dest == []:
                    dest.append(sour.pop())
                elif sour == []:
                    sour.append(dest.pop())
                elif dest[-1] < sour[-1]:
                    sour.append(dest.pop())
                else:
                    dest.append(sour.pop())
            if i % 3 == 2:
                if buff == []:
                    buff.append(sour.pop())
                elif sour == []:
                    sour.append(buff.pop())
                elif buff[-1] < sour[-1]:
                    buff.append(sour.pop())
                else:
                    sour.append(buff.pop())
            if i % 3 == 0:
                if buff == []:
                    dest.append(buff.pop())
                elif dest == []:
                    buff.append(dest.pop())
                elif buff[-1] < dest[-1]:
                    dest.append(buff.pop())
                else:
                    buff.append(dest.pop())
            print(i, sour, buff, dest)
    if n % 2 == 0:
        for i in range(2 ** n):
            if i % 3 == 1:
                if buff == []:
                    buff.append(sour.pop())
                elif buff[-1] < sour[-1]:
                    buff.append(sour.pop())
                else:
                    sour.append(buff.pop())
            if i % 3 == 2:
                if dest == []:
                    dest.append(sour.pop())
                elif dest[-1] < sour[-1]:
                    dest.append(sour.pop())
                else:
                    sour.append(dest.pop())
            if i % 3 == 0:
                if dest == []:
                    dest.append(buff.pop())
                elif dest[-1] < buff[-1]:
                    dest.append(buff.pop())
                else:
                    buff.append(dest.pop())


if __name__ == "__main__":
    sour = "sour"
    buff = "buff"
    dest = "dest"

    hanoi_rec(3, sour, dest, buff)
    hanoi_ite(4)
