class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        length=len(nums)
        for idx in range(length):
            nums.append(int(str(nums[idx])[::-1]))
        count=Counter(nums)
        return len(count)
