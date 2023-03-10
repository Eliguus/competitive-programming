class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def good(mid):
            count=0
            for i in piles:
                count+=ceil(i/mid)
            return count<=h

        left=1
        right=max(piles)
        while left+1<right:
            mid=left+(right-left)//2
            if good(mid):
                right=mid

            else:
                left=mid+1

        return left if good(left) else right
