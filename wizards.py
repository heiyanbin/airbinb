__author__ = 'heiyanbin'
import sys
import Queue


def djsk(wizards, s, t):
    n = len(wizards)
    d = [sys.maxint] * n
    d[s] = 0
    q = Queue.PriorityQueue()
    q.put((d[s], s))

    while q.qsize() > 0:
        dx, v = q.get()
        if dx > d[v]: continue
        for e in wizards[v]:
            cost = (e - v) ** 2
            if d[v] + cost < d[e]:
                d[e] = d[v] + cost
                q.put((d[e], e))
    return d[t]

wizards = [
        [1, 4, 5],
        [],
        [],
        [],
        [9],
        [],
        [],
        [],
        [],
        []
]
print djsk(wizards, 0, 9)




