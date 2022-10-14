class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxLength=0
        left=0
        right=0
        count=0
        while right<len(nums):
            while count<=1 and right<len(nums):
                if  nums[right]==0:
                    count+=1
                right+=1
            if count==2:
                maxLength=max(maxLength,right-left-2)
            else:
                maxLength=max(maxLength,right-left-1)
            left+=1
            if nums[left-1]==0:
                count-=1
        
        return maxLength
                
