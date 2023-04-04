class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        d = 2

        while d*d<=n:

            while n%d==0:
                n//=d
                ans+=d
            d+=1
        if n>1:
            ans+=n
        
        return ans
