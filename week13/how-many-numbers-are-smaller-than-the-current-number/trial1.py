class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=[0]*(max(nums)+1)
        for num in nums:
            count[num]+=1
        for idx,num in enumerate(nums):
            nums[idx]=sum(count[:num])
        return nums
