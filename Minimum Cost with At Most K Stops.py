__author__ = 'heiyanbin'
import sys
def minCostPath(lines, src, dst, maxStops):
    # build adjacent list
    adj = {}
    for a, b, cost in lines:
        if a not in adj: adj[a] = []
        adj[a].append((b, cost))

    minPath = [sys.maxint, []]
    def dfs(v, sumCost, path):
        if v == dst: minPath[0], minPath[1] = sumCost, path[:]
        elif v in adj and len(path) < maxStops + 1:
            for to, cost in adj[v]:
                if to not in path and sumCost + cost < minPath[0]:
                    dfs(to, sumCost + cost, path + [to])

    dfs(src, 0, [src])
    return minPath


def minCostPathByDP(lines, src, dst, maxStops):
    # build adjacent list
    adj = {};
    for a, b, cost in lines:
        if a not in adj: adj[a] = []
        adj[a].append((b, cost))

    memo = {}
    def f(x, y):
        if x == dst: return 0, [dst]
        if x in memo and y in memo[x]: return memo[x][y]
        if x not in memo: memo[x] = {}
        memo[x][y] = (sys.maxint, [])
        if x in adj and y > 0:
            for to, cost in adj[x]:
                s, path = f(to, y - 1)
                if s + cost < memo[x][y][0]: memo[x][y] = (s + cost, [x] + path)
        return memo[x][y]
    return f(src, maxStops)

lines = [('BJ', 'SH', 100), ('SH', 'XA', 20), ('BJ', 'XA', 500), ('TJ', 'SH', 200), ('TJ', 'XA', 50), ('BJ', 'TJ', 100)]
lines2 = [('A', 'B', 100), ('A', 'C', 400), ('B', 'C', 100), ('C', 'D', 100), ('C', 'A', 10)]
print (minCostPathByDP(lines2, 'A', 'D', 2))
