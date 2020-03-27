
maxNum = ['0']
def combineMax(nums, k):
    nums = list(nums)
    def dfs(start, count, curNum):
        global  maxNum
        if start == len(nums) or count == k:
            if len(curNum) > len(maxNum) or len(curNum) == len(maxNum) and curNum > maxNum:
                print maxNum, curNum
                maxNum = curNum
        else:
            for i in range(start, len(nums)):
                dfs(i + 1, count + 1, curNum + list(nums[i]))

    dfs(0, 0, [])
    return ''.join(maxNum)

nums = ['123', '2', '5']
print combineMax(nums, 5)