class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l=0
        r=int(c**0.5)
        while l<=r:
            if l**2+r**2>c:
                r-=1
            elif l**2+r**2<c:
                l+=1
            else:
                return True
        return False
