
def minStartSet(edges):
    inSet = set()
    all = set()
    adj = {}
    for s, e in edges:
        if s not in adj: adj[s] = []
        adj[s].append(e)
        if s != e: inSet.add(e)
        all.add(e)
        all.add(s)

    minSet = all - inSet
    marked = set()
    def dfs(v):
        marked.add(v)
        if v in adj:
            for u in adj[v]:
                if u not in marked:
                    dfs(u)

    for v in minSet:
        if v not in marked:
            dfs(v)

    loopSet = all - marked
    marked.clear()
    for v in loopSet:
        if v not in marked:
            dfs(v)
            minSet.add(v)

    return minSet

case1 = ((0, 1), (1, 0), (2, 1), (3, 1), (3, 2))
case2 = ((2, 9), (3, 3), (3, 5), (3, 7), (4, 8), (5, 8), (6, 6), (7, 4), (8, 7), (9, 3), (9, 6))
g = [[1, 1, 0, 0, 0, 0],
          [1, 1, 1, 0, 0, 0],
          [0, 0, 1, 0, 0, 0],
          [0, 1, 0, 1, 0, 0],
          [0, 0, 0, 0, 1, 1],
          [0, 0, 0, 0, 0, 1]]
case3 = []
for i in range(len(g)):
    for j in range(len(g[0])):
        if g[i][j] == 1: case3.append((i, j))

case4 = [(0, 1), (0, 2), (3, 4), (4, 3), (5, 6), (6, 5)]

print minStartSet(case4)




