class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        summ=0
        ans=100000000
        while r<len(nums):
            summ+=nums[r]
            while summ>=target:
                summ-=nums[l]
                
            
                ans=min(ans,r-l+1)
                l+=1
            r+=1
        return ans if ans!=100000000 else 0
            
