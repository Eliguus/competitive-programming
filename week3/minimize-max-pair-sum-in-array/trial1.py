class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums=sorted(nums)
        return nums[0]+nums[-1]
