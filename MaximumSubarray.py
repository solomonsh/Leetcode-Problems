from cmath import inf


class Solution:

    def maxSubArray(self, nums):
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)

        return maxSub


sol = Solution()

nums = [-2, 1]

print(sol.maxSubArray(nums))
