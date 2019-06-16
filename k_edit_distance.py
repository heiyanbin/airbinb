def kEditDistanceWords(dict, target, k):
    ans = []
    visited = set()
    def dfs(i, word):
        if word in visited:
            return
        visited.add(word)
        if i == k:
            if word in dict: ans.append(word)
        else:
            for j in range(len(target) + 1):
                for c in map(chr, range(ord('a'), ord('z') + 1)):
                    if j < len(target) and target[j] != c:
                        dfs(i + 1, target[:j] + c + target[j + 1:])

                    dfs(i + 1, target[:j] + c + target[j:])

                dfs(i + 1, target[:j] + target[j + 1:])
    dfs(0, target)
    return ans

dict = ("abcd", "aabc", "abbc", "accc", "bbc")
target = "abc"

print kEditDistanceWords(dict, target, 1)