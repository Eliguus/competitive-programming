class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counted = Counter(nums)

        for key,val in counted.items():
            if val==1:
                return key
