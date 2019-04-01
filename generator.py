import numpy as np


def _get_inv_count(arr):
    inv_count = 0
    for i in range(0, 15):
        for j in range(i + 1, 16):
            if arr[i] != 0 and arr[j] != 0 and arr[i] > arr[j]:
                inv_count += 1
    return inv_count


def _find_x_pos(arr):
    for i in arr:
        if arr[i] == 0:
            return 4 - int(i / 4)


def is_solvable(arr):
    inv_count = _get_inv_count(arr)
    pos = _find_x_pos(arr)

    if pos % 2 == 0:
        if inv_count % 2 != 0:
            return True
    else:
        if inv_count % 2 == 0:
            return True

    return False


def generate_puzzle(stub=True):
    if not stub:
        while True:
            arr = np.random.permutation(16)
            if is_solvable(arr):
                return str(list([list(x) for x in np.reshape(arr, (4, 4))]))
    return str([
        [1, 2, 6, 3],
        [4, 9, 5, 7],
        [8, 13, 11, 15],
        [12, 14, 0, 10]
    ])
