class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        prefix = 2 ** 31 - 1
        res = 0
        for num in nums:
            prefix &= num
            if prefix == 0:
                res += 1
                prefix = 2 ** 31 - 1
        
        return max(1, res)