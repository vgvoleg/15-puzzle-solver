
def h_misplaced(state):
    """
    Counts the number of misplaced tiles
    """
    misplaced = 0
    compare = 0
    m = eval(state)
    for i in range(4):
        for j in range(4):
            if m[i][j] != compare:
                misplaced += 1
            compare += 1
    return misplaced


def h_manhattan(state):
    """
    Manhattan distance
    """
    distance = 0
    m = eval(state)
    for i in range(4):
        for j in range(4):
            if m[i][j] == 0:
                continue
            distance += abs(i - (m[i][j] / 4)) + abs(j - (m[i][j] % 4))
    return distance
