import sys
def shortestPath(board):
    m, n = len(board), len(board[0])
    inPath = [[0] * n for _ in range(m)]
    count = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == 2: count += 1

    minLen = [sys.maxint]
    def dfs(i, j, pathLen, eaten):
        inPath[i][j] += 1
        if (i, j) == (m - 1, n - 1):
            if eaten == count: minLen[0] = min(minLen[0], pathLen)
        else:
            for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + dir[0], j + dir[1]
                if x >= 0 and x < m and y >= 0 and y < n and inPath[x][y] < 2 and board[x][y] != 1:
                    dfs(x, y, pathLen + 1, eaten + (1 if board[x][y] == 2 else 0))
        inPath[i][j] -= 1

    dfs(0, 0, 1, 1 if board[0][0] == 2 else 0)
    return minLen[0]

board = [
    [0, 0, 2, 1],
    [1, 2, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 1, 0]
]

print shortestPath(board)









