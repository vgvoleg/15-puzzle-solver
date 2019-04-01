from solver import AStarSolver
from heuristic import h_manhattan, h_misplaced
from generator import generate_puzzle

import numpy as np


def print_board(board):
    print(np.matrix(eval(board)))


def print_result(result):
    import os
    import time

    print("Solution found! It contains {} steps. Press enter to print result".format(len(result)))
    input()
    for step in result:
        os.system('clear')
        print_board(step)
        time.sleep(0.12)


if __name__ == '__main__':
    final_state = str([
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14, 15]
    ])

    solver = AStarSolver(h_manhattan, final_state)
    puzzle = generate_puzzle(s)
    print("Try to solve this puzzle:")
    print_board(puzzle)
    res = solver.solve(puzzle)
    print_result(res)

