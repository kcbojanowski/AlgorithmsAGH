import math


class circle:
    def __init__(self, r=0):
        self.r = r

    def cir_area(self):
        return math.pi * float(self.r) * float(self.r)

    def cir_circuit(self):
        return 2 * math.pi * float(self.r)


class triangle:
    def __init__(self, a=0, h=0):
        self.a = a
        self.h = h

    def tri_area(self):
        return float(self.a) * float(self.h) / 2

    def tri_circuit(self):
        return float(self.a) * 3


class square:
    def __init__(self, a=0):
        self.a = a

    def sqe_area(self):
        return float(self.a) ** 2

    def sqe_circuit(self):
        return float(self.a) * 4
