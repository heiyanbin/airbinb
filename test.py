__author__ = 'heiyanbin'

def minCostPath(lines, src, dst, maxStops):
    adj = {}
    for line in lines:
        (a, b, cost) = line
        if a not in adj:
            adj[a] = []
        adj[a].append((b, cost))

    v = 1
    minPath = []
    minCost = 10000
    def f():
        minCost = 'ff'
        print v, minCost

    def f2():
        minCost = 1
        if v == dst:
            minCost = cost
            minPath = path[:]
        elif v in adj and len(path) < maxStops:
            for line in adj[v]:
                if line[0] not in path and cost + line[1] < minCost:
                    dfs(line[0], cost + line[1], path + [line[0]])
    f()

def minCostPath(lines, src, dst, maxStops):
    adj = {}
    for line in lines:
        (a, b, cost) = line
        if a not in adj:
            adj[a] = []
        adj[a].append((b, cost))

    minPath = []
    minCost = 10000
    s = 0
    def dfs(v, cost, path):
        minCost = 1
        if v == dst:
            minCost = cost
            minPath = path[:]
        elif v in adj and len(path) < maxStops:
            for line in adj[v]:
                if line[0] not in path and cost + line[1] < minCost:
                    dfs(line[0], cost + line[1], path + [line[0]])

    dfs(src, 0, [src])

    def f():
        s = 2
    f()
    return minPath, minCost, s

lines = [('BJ', 'SH', 100), ('SH', 'XA', 200), ('BJ', 'XA', 500), ('TJ', 'SH', 200), ('TJ', 'XA', 50)]

print(minCostPath(lines, 'BJ', 'XA', 2))
test()