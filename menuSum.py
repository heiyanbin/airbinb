__author__ = 'heiyanbin'

def menuCombination(menu, sum):
    ans = []
    def dfs(i, curSum, picked):
        if curSum == sum:
            ans.append(picked)
        elif i < len(menu):
            if curSum < sum:
                dfs(i + 1, curSum, picked)
            if curSum + menu[i] <= sum:
                dfs(i + 1, curSum + menu[i], picked + [i]) # a item could only be picked once
              # dfs(i, curSum + menu[i], picked + [i]) a item could be picked as many times
    dfs(0, 0, [])
    return ans

print menuCombination([1, 3, 4, 5, 9], 10)


