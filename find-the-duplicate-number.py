class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums=Counter(nums)
        for key,value in nums.items():
            if value>=2:
                return key