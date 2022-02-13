import math
import random
import Visualize_tsp
import numpy as np
from time import time

# Salesman Problem solved using Simulated Annealing Algorithm and compering it wth Greedy Algorithm
# Data used: TSP.txt

class SimAnneal(object):
    def __init__(self, cords, start=1, t=-1, alpha=-1, stopping_t=-1, stopping_iter=-1):
        self.start = start
        self.coords = cords
        self.N = len(cords)
        self.T = math.sqrt(self.N) if t == -1 else t
        self.alpha = 0.995 if alpha == -1 else alpha
        self.stopping_temperature = 1e-8 if stopping_t == -1 else stopping_t
        self.stopping_iter = 100000 if stopping_iter == -1 else stopping_iter
        self.iteration = 1
        self.T_save = self.T
        self.nodes = [i for i in range(self.N)]
        self.best_solution = None
        self.best_rating = np.inf
        self.rating_list = []
        self.greedy_path = []

    def greedy_algo(self):

        cur_node = 0
        solution = [cur_node]
        free_nodes = list(self.nodes)
        free_nodes.remove(cur_node)
        while free_nodes:
            next_node = min(free_nodes, key=lambda x: self.dist(cur_node, x))
            free_nodes.remove(next_node)
            solution.append(next_node)
            cur_node = next_node

        cur_fit = self.fit(solution)
        if cur_fit < self.best_rating:
            self.best_rating = cur_fit
            self.best_solution = solution
        self.rating_list.append(cur_fit)
        return solution, cur_fit

    def greedy_algo2(self):
        start = 1
        solution = [start]
        lst_nodes = list(self.nodes)
        lst_nodes.remove(start)

        cost = np.inf
        pom = 0
        moves = [start]
        for i in range(99):
            for x in range(len(lst_nodes)):
                moves.append(lst_nodes[x])
                koszt = self.pathing(moves)
                moves.remove(moves[1])
                if koszt < cost:
                    cost = koszt
                    pom = lst_nodes[x]
            moves.append(pom)
            moves.remove(moves[0])
            solution.append(moves[0])
            lst_nodes.remove(moves[0])
            cost = np.inf
        solution.append(start)
        cur_fit = self.pathing(solution)
        if cur_fit < self.best_rating:
            self.best_rating = cur_fit
            self.best_solution = solution
            self.rating_list.append(cur_fit)
        self.greedy_path = solution
        print("greedy algorithm route: ", solution)
        print("cost of greedy algorithm: ", cur_fit)
        return solution, cur_fit

    def dist(self, node_0, node_1):

        coord_0, coord_1 = self.coords[node_0], self.coords[node_1]
        x = coord_0[0] - coord_1[0]
        y = coord_0[1] - coord_1[1]
        xy = np.array([x, y])
        meg = np.linalg.norm(xy)
        return meg

    def pathing(self, moves):
        cost = 0
        for i in range(1, len(moves)):
            x = self.coords[moves[i - 1] - 1][0] - self.coords[moves[i] - 1][0]
            y = self.coords[moves[i - 1] - 1][1] - self.coords[moves[i] - 1][1]
            xy = np.array([x, y])
            mag = np.linalg.norm(xy)
            cost += mag
        return cost

    def fit(self, solution):
        cur_fit = 0
        for i in range(self.N):
            cur_fit += self.dist(solution[i % self.N], solution[(i + 1) % self.N])
        return cur_fit

    def p_jury(self, candidate_rank):
        return math.exp(-abs(candidate_rank - self.cur_rating) / self.T)

    def jury(self, candidate):
        candidate_rating = self.fit(candidate)
        if candidate_rating < self.cur_rating:
            self.cur_rating, self.cur_solution = candidate_rating, candidate
            if candidate_rating < self.best_rating:
                self.best_rating, self.best_solution = candidate_rating, candidate
        else:
            if random.random() < self.p_jury(candidate_rating):
                self.cur_rating, self.cur_solution = candidate_rating, candidate

    def anneal(self):
        self.cur_solution, self.cur_rating = self.greedy_algo()

        print("Starting annealing.")
        while self.T >= self.stopping_temperature and self.iteration < self.stopping_iter:
            candidate = list(self.cur_solution)
            l = random.randint(2, self.N - 1)
            i = random.randint(0, self.N - l)
            candidate[i:(i + l)] = reversed(candidate[i:(i + l)])
            self.jury(candidate)
            self.T *= self.alpha
            self.iteration += 1

            self.rating_list.append(self.cur_rating)
        print("Best cost of SA: ", self.best_rating)
        improvement = 100 * (self.rating_list[0] - self.best_rating) / (self.rating_list[0])
        print(f"Improvement over greedy algorithm: {improvement : .2f}%")

    def graphs(self):
        Visualize_tsp.plot_AS(self.best_solution, self.coords, 5)
        Visualize_tsp.plot_greedy(self.greedy_path, self.coords)

    def multiple_anneal(self, times=10):
        times_anneal = []
        for i in range(1, times + 1):
            print(f"Iteration {i}/{times} -------------------------------")
            self.T = self.T_save
            self.iteration = 1
            self.cur_solution, self.cur_rating = self.greedy_algo()
            start_anneal = time()
            self.anneal()
            stop_anneal = time() - start_anneal
            print(f"Time of Iteration is {stop_anneal}")
            times_anneal.append(stop_anneal)
        avg = np.average(np.array(times_anneal))
        print(f"\nAverage Time of Simulated Annealing: {avg}")



def read_coords(path):
    cities = open(path, "r")
    lines = cities.readlines()
    string_data = [line.strip().split() for line in lines]
    data = np.array(string_data).astype(float)
    data = np.delete(data, 0, 1)
    return data


if __name__ == "__main__":
    coords = read_coords("TSP.txt")
    sa = SimAnneal(coords, 1, stopping_iter=5000)
    start_greedy = time()
    sa.greedy_algo2()
    stop_greedy = time() - start_greedy
    sa.multiple_anneal(10)
    print(f"Time of Greedy Iteration: {stop_greedy}")
    sa.graphs()
