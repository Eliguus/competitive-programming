class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        sort=sorted(nums)
        count=0
        for i in range(len(sort)-1):
            if sort[i]>=sort[i+1]:
                count+=sort[i]-sort[i+1]+1
                sort[i+1]=sort[i]+1
                 
        return count
