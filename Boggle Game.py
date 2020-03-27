# from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.value = None
        self.next = {}  # defaultdict(lambda:None)


class Solution:
    """
    @param: board: a list of lists of character
    @param: words: a list of string
    @return: an integer
    """

    def boggleGame(self, board, words):
        # write your code here
        m, n = len(board), len(board[0])

        def put(root, key, i):
            if root == None: root = TrieNode()
            if i == len(key):
                root.value = True
            else:
                if key[i] not in root.next:
                    root.next[key[i]] = None
                root.next[key[i]] = put(root.next[key[i]], key, i + 1)
            return root

        root = TrieNode()
        for word in words:
            put(root, word, 0)

        def inOrder(root, path):
            if root.value: print path
            for link in root.next:
                inOrder(root.next[link], path + link)

        inOrder(root, '')

        inPath = [[False] * n for _ in range(m)]
        count = [0]
        def dfs(i, j, node, path):
            if board[i][j] not in node.next: return 0
            count[0] += 1
            print i, j, path, inPath
            inPath[i][j] = True
            node = node.next[board[i][j]]
            maxCount = 0
            if node.value:
                maxCount = 1
                for x in xrange(m):
                    for y in xrange(n):
                        if not inPath[x][y]:
                            maxCount = max(1 + dfs(x, y, root, path + [board[i][j]]), maxCount)
            else:
                for dir in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    s, t = i + dir[0], j + dir[1]
                    if s >= 0 and s < m and t >= 0 and t < n and not inPath[s][t] and board[s][t] in node.next:
                        maxCount = max(dfs(s, t, node, path + [board[i][j]]), maxCount)

            inPath[i][j] = False
            return maxCount

        ans = 0
        for i in xrange(m):
            for j in xrange(n):
                    ans = max(ans, dfs(i, j, root, []))
        print count
        return ans

board = ["aa","aa"]
dict = ["a"]
print Solution().boggleGame(board, dict)

