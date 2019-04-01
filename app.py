from solver import AStarSolver
from heuristic import h_manhattan, h_misplaced


def generate_puzzle():
    return str([
        [1, 2, 6, 3],
        [4, 9, 5, 7],
        [8, 13, 11, 15],
        [12, 14, 0, 10]
    ])


def print_result(result):
    import numpy as np
    import os
    import time
    for step in result:
        os.system('clear')
        print(np.matrix(eval(step)))
        time.sleep(0.2)


if __name__ == '__main__':
    final_state = str([
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14, 15]
    ])

    solver = AStarSolver(h_manhattan, final_state)
    puzzle = generate_puzzle()
    res = solver.solve(puzzle)
    print_result(res)

