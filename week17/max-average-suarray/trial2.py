class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        temp_sum=max_sum
        for idx in range(k,len(nums)):
            max_sum = max_sum-nums[idx-k]+nums[idx]
            temp_sum=max(max_sum,temp_sum)
        return temp_sum/k
