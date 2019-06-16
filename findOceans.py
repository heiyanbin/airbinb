__author__ = 'heiyanbin'

def findOceans(board, x, y):
    #mark = [[-1] * len(board[0]) for _ in range(len(board))]
    def dfs(i, j):
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or board[i][j] == 'L' or board[i][j] == 'O': return
        board[i][j] = 'O'
        for dir in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            dfs(i + dir[0], j + dir[1])

    dfs(x, y)


board = map(list, ["WWWLLLW",
         "WWLLLWW",
         "WLLLLWW"])

for row in board:
    print row
findOceans(board, 0, 1)
print '=================='
for row in board:
    print row

