class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        idx=0
        while idx<len(nums):
            if idx<len(nums)-1 and nums[idx]==nums[idx+1] and nums[idx]!=0:
                nums[idx]*=2
                nums.pop(idx+1)
                nums.append(0)
            idx+=1
        right=0
        left=0
        for right in range(len(nums)):
            if nums[left]!=0:
                left+=1
            elif nums[left]==0 and nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
        
        return nums
