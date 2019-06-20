from copy import deepcopy

def f(n):
    if n < 2: return 1
    return f(n -1) + f(n - 2);

def group(A, k):
    if k == 1:return [[A[:]]]
    if k == len(A): return [map(lambda x: [x], A)]
    last = A.pop()
    groupings = group(A, k - 1)
    for grouping in groupings: grouping.append([last])

    for grouping in group(A, k):
        for g in grouping:
            g.append(last)
            groupings.append(deepcopy(grouping))
            g.pop()
    A.append(last)
    return groupings

for grouping in group([1, 2, 3, 4], 2):
    print grouping