def findMissingRanges(nums, lower, upper):
    # write your code here
    ans = []
    pre = lower - 1
    if len(nums) > 0 and upper - nums[-1] > 1 or len(nums) == 0:
        nums.append(upper + 1)
    for num in range(len(nums)):
        if num != pre + 1:
            if num - pre == 2:
                ans.append(str(pre + 1))
            elif num - pre > 2:
                ans.append(str(pre + 1) + '->' + str(num - 1))
        pre = num
    return ans

print(findMissingRanges([], 1, 1))