import module_2 as m


if __name__ == "__main__":

    c = input("circle's radius: ")
    pole = m.circle(c)
    print("circle's area: ", pole.cir_area())
    print("circle circuit: ", pole.cir_circuit())

    t = input("triangle's edge: ")
    t2 = input("triangle's height: ")

    pole2 = m.triangle(t, t2)
    print("triangle area", pole2.tri_area())
    print("triangle circuit", pole2.tri_circuit())

    s = input("square's edge: ")
    pole3 = m.square(s)
    print("square area", pole3.sqe_area())
    print("square circuit", pole3.sqe_circuit())
