from copy import deepcopy


def printZMatrix(self, matrix):
    # write your code here
    m, n = len(matrix), len(matrix[0])
    move = ((1, -1), (-1, 1))
    dir = 1
    i, j = 0, 0
    ans = []
    while i >= 0 and i < m and j >= 0 and j < n:
        ans.append(matrix[i][j])
        newi, newj = i + move[dir][0], j + move[dir][1]
        if newj >= 0 and newj < n and newi >= 0 and newi < m:
            i, j = newi, newj
        else:
            dir ^= 1
            if newj < 0 or newj == n and newi < 0 or newi == m:
                if i + 1 >= 0 and i + 1 < m:
                    i += 1
                else:
                    j += 1
            elif newj < 0 or newj == n:
                i += 1
            else:
                j += 1
    return ans

a = [
    [1, 2,  3,  4],
    [5, 6,  7,  8],
    [9,10, 11, 12]
  ]
print printZMatrix(0, a)


class Solution:
    """
    @param words: an array of string
    @param maxWidth: a integer
    @return: format the text such that each line has exactly maxWidth characters and is fully
    """

    def fullJustify(self, words, maxWidth):
        # write your code here
        ans = []
        i = 0
        while i < len(words):
            l, num = 0, 0
            while i + num < len(words) and l + len(words[i + num]) <= maxWidth - num:
                l += len(words[i + num])
                num += 1
            line = list(words[i])
            for k in range(1, num):
                padding = [' '] * ((maxWidth - l) / num)
                if k < (maxWidth - l) % num:
                    padding.append(' ')
                line.extend(padding)
                line.extend(words[i + k])
                line.extend(' ' * (maxWidth - len(line)))
                ans.append(''.join(line))
                i += num + 1
        return ans

def getMaxScore(self, x, y, cost, profit):
    # Write your code here
    n = len(profit)
    adj = [{} for _ in xrange(n)]
    for i in xrange(len(x)):
        adj[x[i]][y[i]] = cost[i]

    print adj

    def dfs(i):
        print i
        if len(adj[i]) == 0:
            return profit[i]
        maxScore = profit[i]
        for v, cost in adj[i].iteritems():
            maxScore = max(maxScore, profit[i] - cost + dfs(v))

        return maxScore

    return dfs(0)

print getMaxScore(0,[0,1,2,3], [1,2,3,4], [4,2,3,5],[1,8,7,2])