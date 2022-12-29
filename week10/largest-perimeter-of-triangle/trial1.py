class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for idx in range(len(nums)-2):
            if nums[idx]<nums[idx+1]+nums[idx+2]:
                return nums[idx]+nums[idx+1]+nums[idx+2]
        return 0
