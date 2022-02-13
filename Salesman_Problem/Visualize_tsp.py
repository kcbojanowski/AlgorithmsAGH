import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

# class used to visualize graphs of Salesman Problem

def plot_AS(paths, points, num_iters):
    x = []
    y = []
    for i in paths:
        x.append(points[i][0])
        y.append(points[i][1])
    plt.plot(x, y, 'bo')
    a_scale = float(max(x)) / float(100)

    if num_iters > 1:
        for i in range(1, num_iters):
            xi = []
            yi = []
            for j in paths:
                xi.append(points[j][0])
                yi.append(points[j][1])

            plt.arrow(xi[-1], yi[-1], (xi[0] - xi[-1]), (yi[0] - yi[-1]),
                      head_width=a_scale, color='r',
                      length_includes_head=True, ls='dashed',
                      width=0.001 / float(num_iters))
            for i in range(0, len(x) - 1):
                plt.arrow(xi[i], yi[i], (xi[i + 1] - xi[i]), (yi[i + 1] - yi[i]),
                          head_width=a_scale, color='r', length_includes_head=True,
                          ls='dashed', width=0.001 / float(num_iters))

    plt.arrow(x[-1], y[-1], (x[0] - x[-1]), (y[0] - y[-1]), head_width=a_scale,
              length_includes_head=True)
    for i in range(0, len(x) - 1):
        plt.arrow(x[i], y[i], (x[i + 1] - x[i]), (y[i + 1] - y[i]), head_width=a_scale,
                  length_includes_head=True)
    plt.title("Simulated Annealing Algorithm")
    plt.grid(True)
    plt.savefig("AS_graph.png")
    plt.show()


def plot_greedy(moves, cords):
    points = []
    cods = []
    for elem in moves:
        points.append((float(cords[elem - 1][0]), float(cords[elem - 1][1])))
    cods.append(Path.MOVETO)
    for x in range(len(moves) - 2):
        cods.append(Path.LINETO)
    cods.append(Path.CLOSEPOLY)
    path_n = Path(points, cods)
    fig, ax = plt.subplots()
    patch = patches.PathPatch(path_n, facecolor='none', lw=1)
    ax.add_patch(patch)
    for k in range(len(points)):
        plt.plot(points[k][0], points[k][1], 'go')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    plt.title("Greedy Algorithm")
    plt.grid(True)
    plt.savefig("greedy_graph.png")
    plt.show()
