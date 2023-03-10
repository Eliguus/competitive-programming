class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def good(mid):
            summ=0
            for i in nums:
                summ+=ceil(i/mid)

            return summ<=threshold

        right=max(nums)
        left=1
        while left<right:
            mid=left+(right-left)//2
            if good(mid):
                right=mid
            else:
                left=mid+1
        return right
