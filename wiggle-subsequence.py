class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        preDif = nums[1] - nums[0]
        if preDif != 0:
            total = 2
        else:
            total = 1
        for idx in range(2,len(nums)):
            dif = nums[idx] - nums[idx-1]

            if (dif > 0 and preDif <= 0) or (dif < 0 and preDif >= 0):
                total += 1
                preDif = dif
        
        return total