class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums=sorted(nums)
        sum=[]
        for i in range(int(len(nums)/2)):
            sum+=[nums[i]+nums[-1-i]]
        return max(sum)
            
