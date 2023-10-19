class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def cal(index,target):
            if index == len(nums):
                return target == 0
            return cal(index+1,target - nums[index]) or cal(index+1,target)
        s = sum(nums)

        if s % 2 : return False

        target = s // 2
        return cal(0,target)