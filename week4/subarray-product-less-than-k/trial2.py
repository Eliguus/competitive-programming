class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1: return 0
        count=0
        
        l=0
        r=0
        pro=1
        
        for r in range(len(nums)):
            pro*=nums[r]
           
            
            while pro>=k:
                
                pro/=nums[l]
                l+=1
            count+=r-l+1
            
        return count
                
        
