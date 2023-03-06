class Solution:
    def mySqrt(self, x: int) -> int:
        r=x
        l=0
        while l<=r:
            mid = l+(r-l)//2

            if mid**2>x:
                r=mid-1

            elif mid**2<x:
                l=mid+1
            
            else:
                return mid
        return r
