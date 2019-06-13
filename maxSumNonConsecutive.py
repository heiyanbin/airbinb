def maxSumNonConsecutive(A):
    #f(i) = max(f(i - 2) + A[i-1], f(i - 1))
    if len(A) == 0: return 0
    f2 = 0
    f1 = A[0]
    for i in range(2, len(A) + 1):
        f = max(f2 + A[i - 1], f1)
        f2 = f1
        f1 = f
    return f

print(maxSumNonConsecutive([5, 2, 3, 5, 3]))