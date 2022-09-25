class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        left=0
        right=0
        ans=0
        summ=0
        while right<len(nums):
            summ+=nums[right]
            while nums[right]*(right-left+1)>k+summ:
                summ-=nums[left]
                left+=1
            ans=max(ans,right-left+1)
            
            right+=1
        return ans
