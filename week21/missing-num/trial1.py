class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        original = []

        for num in range(len(nums)+1):
            original.append(-1)

        for num in nums:
            original[num]=num

        for i in range(len(original)):
            if original[i]==-1:
                return i
