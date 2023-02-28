class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        s=0
        d={0:1}
        ans=0
        
        for i in nums:
            s+=i
            ans+=d.get(s%k,0)
            d[s%k]=d.get(s%k,0)+1
        return ans
