
def triangle(n):
    if n == 1:
        return [
            [' ', '/', '\\', ' '],
            ['/', '_', '_', '\\']
        ]
    else:
        unit = triangle(n - 1)
        m = len(unit)
        n = len(unit[0])
        ans = [[' '] * n * 2 for _ in range(m * 2)]
        for i in range(m):
            for j in range(n):
                ans[i][j + n / 2] = unit[i][j]
            for j in range(n):
                ans[i + m][j] = unit[i][j]
            for j in range(n):
                ans[i + m][j + n] = unit[i][j]
        return ans


for line in triangle(2):
   # print line
    print ''.join(line)
