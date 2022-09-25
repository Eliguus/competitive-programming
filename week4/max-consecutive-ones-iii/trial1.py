class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        ans=0
        total=0
        while r<len(nums):
            total+=nums[r]
            while r-l+1>total+k:
                total-=nums[l]
                l+=1
            ans=max(ans,r-l+1)
            r+=1
        return ans
            
