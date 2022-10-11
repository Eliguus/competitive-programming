class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ind2=0
        ans=0
        nice=0
        num_odd=0
        for ind1 in range(len(nums)):
            if nums[ind1]%2:
                num_odd+=1
                nice=0
            while num_odd==k:
                num_odd-=nums[ind2]%2
                ind2+=1
                nice+=1
            ans+=nice
        return ans
                
