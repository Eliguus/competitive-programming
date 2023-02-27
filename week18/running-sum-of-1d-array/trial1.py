class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for idx in range(len(nums)-1):
            nums[idx+1]+=nums[idx]
        return nums
