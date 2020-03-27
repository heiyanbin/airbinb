__author__ = 'heiyanbin'

def caseCombination(s):
    ans = []
    def dfs(i, path):
        if i == len(s):
            ans.append(path)
        else:
            dfs(i + 1, path + s[i].lower())
            if s[i].isalpha():
                dfs(i + 1, path + s[i].upper())
    dfs(0, '')
    return ans

print caseCombination('ab_')
