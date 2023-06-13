class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        temp = [-1]*(len(nums)+2)

        for num in nums:
            if num<=len(nums) and num>0:
                temp[num] = 1

        for idx,num in enumerate(temp):
            if num==-1 and idx!=0:
                return idx
        
        return len(nums)