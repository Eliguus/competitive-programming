class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        memo = {}
        def dp1(idx,nums):
            if idx>=len(nums):
                return 0
            if (idx,nums) in memo:
                return memo[(idx,nums)]
            memo[(idx,nums)] = max(nums[idx]+dp1(idx+2,nums),dp1(idx+1,nums))
            return memo[(idx,nums)]
        
        
        return max(dp1(0,tuple(nums[:-1])),dp1(0,tuple(nums[1:])))