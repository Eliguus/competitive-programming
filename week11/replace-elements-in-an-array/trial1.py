class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic={}
        for idx,num in enumerate(nums):
            dic[num]=idx
        for old,new in operations:
            idx=dic[old]
            nums[idx]=new
            dic[new]=idx
            del dic[old]
        return nums
