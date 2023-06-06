class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(i,cur):
            if i == len(nums):
                if cur==target:
                    return 1
                else:
                    return 0
            if (i,cur) not in memo:
                memo[(i,cur)] = dp(i+1,cur+nums[i]) + dp(i+1,cur-nums[i])
                return memo[(i,cur)]

            return memo[(i,cur)]
        return dp(0,0)