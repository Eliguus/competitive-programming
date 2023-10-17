class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        elif n>0:
            if n==1:
                return x
            else:
                if n%2==0:
                    temp=self.myPow(x,n//2)
                    return temp*temp
                else:
                    temp=self.myPow(x,n-1)
                    return x*temp
        elif n<0:
            n=-n
            if n==1:
                return 1/x
            else:
                if n%2==0:
                    temp=self.myPow(x,n/2)
                    res=temp*temp
                else:
                    res=x*self.myPow(x,n-1)
            return 1/res