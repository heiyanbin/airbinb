class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

def mergeTwoInterval( list1, list2):
    # write your code here
    ans = []
    i, j = 0, 0
    while i < len(list1) or j < len(list2):
        if i < len(list1) and (j == len(list2) or list1[i].start < list2[j].start):
            if len(ans) == 0 or list1[i].start > ans[-1].end:
                ans.append(list1[i]);
            else:
                ans[-1].start = max(ans[-1].start, list1[i].start)
                ans[-1].end = max(ans[-1].end, list1[i].end)
            i += 1
        else:
            if len(ans) == 0 or list2[j].start > ans[-1].end:
                ans.append(list2[j])
            else:
                ans[-1].start = max(ans[-1].start, list2[j].start)
                ans[-1].end = max(ans[-1].end, list2[j].end)
            j += 1
    return ans

a = [Interval(1,2),Interval(3,4)]
b = [Interval(2,3),Interval(5,6)]

print(mergeTwoInterval(a, b))