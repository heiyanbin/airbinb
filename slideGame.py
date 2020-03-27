__author__ = 'heiyanbin'

def slide(A):
    def toString(A):
        l = []
        for row in A:
            for col in row:
                l.append(str(col))
        return ''.join(l)
    def fromString(s):
        import math
        n = int(math.sqrt(len(s)))
        mat = [[0] * n for i in range(int(len(s) / n))]
        for k in range(len(s)):
            i = int(k / n)
            j = int(k % n)
            mat[i][j] = s[k]
        return mat
    m, n = len(A), len(A[0])
    import Queue
    q = Queue.Queue()
    s = toString(A)
    i, j = s.index('0') / n, s.index('0') % n
    q.put((toString(A), [(i, j)]))
    visited = set()
    while q.qsize() > 0:
        s, path = q.get()
        if s == '123456780':
            return path
        dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
        mat = fromString(s)
        for move in dir:
            i, j = path[-1][0], path[-1][1]
            x, y = i + move[0], j + move[1]
            if x >= 0 and x < m and y >= 0 and y < n and not s in visited:
                mat[x][y], mat[i][j] = mat[i][j], mat[x][y]
                q.put((toString(mat), path + [(x, y)]))
                mat[x][y], mat[i][j] = mat[i][j], mat[x][y]
    return None

def jigsawPuzzle(self, matrix):
    # Write your code here
    def toString(mat):
        res = []
        for i in range(3):
            for j in range(3):
                res.append(str(mat[i][j]))
        return ''.join(res)

    def fromString(sequence):
        mat = [[''] * 3 for _ in range(3)]
        for i in range(len(sequence)):
            mat[i / 3][i % 3] = sequence[i]
        return mat

    marked = set()

    def dfs(v):
        marked.add(v)
        print marked
        if v == '123456780': return True
        mat = fromString(v)
        k = v.index('0')
        i, j = k / 3, k % 3
        for dir in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            x, y = i + dir[0], j + dir[1]
            if x >= 0 and x < 3 and y >= 0 and y < 3:
                mat[i][j], mat[x][y] = mat[x][y], mat[i][j]
                u = toString(mat)
                if u not in marked:
                    if dfs(u): return True
                mat[i][j], mat[x][y] = mat[x][y], mat[i][j]
        return False

    return 'YES' if dfs(toString(matrix)) else 'NO'

a = [[4,0,2],[5,3,8],[6,1,7]]

import sys
sys.setrecursionlimit(1000)
print sys.getrecursionlimit()
print (jigsawPuzzle(0, a))
