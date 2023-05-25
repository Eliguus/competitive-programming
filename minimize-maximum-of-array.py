class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        sums = 0

        for i,num in enumerate(nums):
            sums+=num
            ans = max(ans,ceil(sums/(i+1)))

        return ans