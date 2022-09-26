class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i==0:
                if 0==sum(nums[1:]):
                    return 0
            elif i==len(nums)-1:
                if 0==sum(nums[:i]):
                    return i
            else:
                if sum(nums[:i])==sum(nums[i+1:]):
                    return i
        return -1
        
