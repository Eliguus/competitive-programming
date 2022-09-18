class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==3 or n==1:
            return True
        if n<3:
            return False
        else:
            n=n/3
            return self.isPowerOfThree(n)
