class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pre={0:1}
        ans=0
        s=0
        for i in nums:
            s+=i
            ans+=pre.get(s-goal,0)
            pre[s]=pre.get(s,0)+1
        return ans
