
class AStarSolver:
    def __init__(self, heuristic, final):
        self.heuristic = heuristic
        self.final = final

    def solve(self, start):
        front = [[self.heuristic(start), start]]
        expanded = []
        path = []
        expanded_nodes = 0
        while front:
            i = 0
            for j in range(1, len(front)):
                if front[i][0] > front[j][0]:
                    i = j
            path = front[i]
            front = front[:i] + front[i + 1:]
            last_node = path[-1]
            if last_node == self.final:
                break
            if last_node in expanded:
                continue
            for k in self._moves(last_node):
                if k in expanded:
                    continue
                newpath = [path[0] + self.heuristic(k) - self.heuristic(last_node)] + path[1:] + [k]
                front.append(newpath)
                expanded.append(last_node)
            expanded_nodes += 1
            print(expanded_nodes)
        return path[1:]

    def _moves(self, mat):
        output = []

        m = eval(mat)
        i = 0
        while 0 not in m[i]:
            i += 1
        j = m[i].index(0)  # blank space (zero)

        if i > 0:
            m[i][j], m[i - 1][j] = m[i - 1][j], m[i][j]  # move up
            output.append(str(m))
            m[i][j], m[i - 1][j] = m[i - 1][j], m[i][j]

        if i < 3:
            m[i][j], m[i + 1][j] = m[i + 1][j], m[i][j]  # move down
            output.append(str(m))
            m[i][j], m[i + 1][j] = m[i + 1][j], m[i][j]

        if j > 0:
            m[i][j], m[i][j - 1] = m[i][j - 1], m[i][j]  # move left
            output.append(str(m))
            m[i][j], m[i][j - 1] = m[i][j - 1], m[i][j]

        if j < 3:
            m[i][j], m[i][j + 1] = m[i][j + 1], m[i][j]  # move right
            output.append(str(m))
            m[i][j], m[i][j + 1] = m[i][j + 1], m[i][j]

        return output