class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(sums,idx):
            if sums>target:
                return 0
            if sums==target:
                return 1
            if (idx,sums) in memo:
                return memo[(idx,sums)]
            result = 0
            for i in range(idx,len(nums)):
                result += dp(sums+nums[i],idx)
            memo[(idx,sums)]=result
            return result
        return dp(0,0)