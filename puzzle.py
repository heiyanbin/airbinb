def puzzle(A):
    m, n = len(A), len(A[0])

    def toString():
        ret = ''
        for line in A:
            ret += ''.join(line)
        return ret

    ans, path = None, []
    visited = set()

    def dfs(i, j):
        if toString() == '123456780':
            ans = path[:]
        else:
            dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
            for move in dir:
                x, y = i + move[0], j + move[1]
                if x >= 0 and x < m and y >= 0 and y < n:
                    A[x][y], A[i][j] = A[i][j], A[x][y]
                    image = toString()
                    if image in visited:
                        A[x][y], A[i][j] = A[i][j], A[x][y]
                        continue

                    visited.add(image);
                    path.append((x, y))
                    dfs(x, y)
                    A[x][y], A[i][j] = A[i][j], A[x][y]
                    path.pop()

    for i in range(m):
        for j in range(n):
            if A[i][j] == '0':
                dfs(i, j)

    return ans


#print(puzzle([['1', '2', '3'], ['4', '5', '6'], ['7', '0', '8']]))

import queue
q = queue.Queue();
q.put(1)
q.put(2)
print(q.)
print(q.get())