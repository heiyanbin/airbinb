__author__ = 'heiyanbin'

class UF:
    def __init__(self, N):
        self.N = N
        self.id = []
        self.sz = []
        self.count = N
        for _ in range(N):
            self.id.append(_)
            self.sz.append(1)

    def root(self, i):
        while  i != self.id[i]:
            self.id[self.id[i]] = self.id[self.id[self.id[i]]]
            i = self.id[self.id[i]]
        return i

    def union(self, i, j):
        rooti = self.root(i)
        rootj = self.root(j)
        if rooti == rootj: return
        if self.sz[i] < self.sz[j]:
            self.id[rooti] = rootj
            self.sz[rootj] += self.sz[rooti]
        else:
            self.id[rootj] = rooti
            self.sz[rooti] += self.sz[rootj]
        self.count -= 1

    def connected(self, i, j):
        return self.root(i) == self.root(j)

    def num(self):
        return self.count


def interSect(rec1, rec2):
    return not (rec1[0][0] > rec2[1][0] or rec1[0][1] < rec2[1][1] or rec1[1][0] < rec2[0][0] or rec1[1][1] > rec2[0][1])

def numConnectedRectangle(recList):
    uf = UF(len(recList))
    for i in range(len(recList)):
        for j in range(i + 1, len(recList)):
            if interSect(recList[i], recList[j]):
                uf.union(i, j)
    return uf.num()

recList = [((0, 3), (3, 0)), ((2, 2), (4, 4)), ((1,1), (2, 2))]
print numConnectedRectangle(recList)