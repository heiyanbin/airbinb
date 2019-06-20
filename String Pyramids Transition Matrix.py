

def canReach(table, leaf):
    memo = {}
    def dfs(s, i, next):
        if len(s) == 1: return s in leaf
        if s in memo: return memo[s]
        if i == len(s) - 1:
            memo[s] = dfs(''.join(next), 0, [])
            return memo[s]
        else:
            if s[i:i+2] not in table: return False
            for option in table[s[i:i+2]]:
                if dfs(s, i + 1, next + [option]): return True
            return False
    return dfs(leaf, 0, [])

table = {
    'AA':'A',
    'AB':'AC',
    'AC':'D',
    'AD':'A',
    'BA':'D',
    'BB':'BC',
    'BC':'A',
    'CD':'B'
}

table = {
    'AA':'AC',
    'AB':'CD',
    'AC':'D',
    'AD':'B',
    'BA':'B',
    'BB':'C',
    'BC':'A',
    'BD':'CD',
    'CA':'A',
    'CB':'C',
    'CC':'D',
    'CD':'B',
    'DA':'BC',
    'DB':'D',
    'DC':'A',
    'DD':'C'

}

print canReach(table, 'DDDD')
