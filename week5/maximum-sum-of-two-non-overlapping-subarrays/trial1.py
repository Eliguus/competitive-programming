class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        for i in range(len(nums)-1):
            nums[i+1]+=nums[i]
        maxf=nums[firstLen-1]
        maxs=nums[secondLen-1]
        maxt=nums[firstLen+secondLen-1]
        for i in range(firstLen+secondLen,len(nums)):
            maxf=max(maxf,nums[i-secondLen]-nums[i-secondLen-firstLen])
            maxs=max(maxs,nums[i-firstLen]-nums[i-secondLen-firstLen])
            maxt=max(maxt,max(maxf+nums[i]-nums[i-secondLen],maxs+nums[i]-nums[i-firstLen]))
        return maxt
