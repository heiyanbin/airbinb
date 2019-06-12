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

print slide([[7, 2, 3], [4, 5, 6], [1, 8, 0]])



