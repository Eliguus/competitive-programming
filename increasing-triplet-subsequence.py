class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = 2**31
        second = 2**31

        for n in nums:
            if n <= first:
                first = n

            elif n<=second:
                second = n

            else:
                return True
        return False