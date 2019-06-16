__author__ = 'heiyanbin'
def minCostPath(lines, src, dst, maxStops):
    adj = {}
    for line in lines:
        (a, b, cost) = line
        if a not in adj:
            adj[a] = []
        adj[a].append((b, cost))

    ret = [1000000, None]
    def dfs(v, cost, path):
        if v == dst:
            ret[0]= cost
            ret[1] = path[:]
        elif v in adj and len(path) < maxStops + 1:
            for line in adj[v]:
                if line[0] not in path and cost + line[1] < ret[0]:
                    dfs(line[0], cost + line[1], path + [line[0]])

    dfs(src, 0, [src])
    return ret

lines = [('BJ', 'SH', 100), ('SH', 'XA', 20), ('BJ', 'XA', 500), ('TJ', 'SH', 200), ('TJ', 'XA', 50), ('BJ', 'TJ', 100)]

print(minCostPath(lines, 'BJ', 'XA', 2))
