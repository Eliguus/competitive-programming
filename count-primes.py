class Solution:
    def countPrimes(self, n: int) -> int:
        prime=[1]*n
        if n==0 or n==1:
            return 0
        for i in range(2,n):
            if prime[i]==1:
                for j in range(i+i,n,i):
                    prime[j]=0
        return sum(prime)-2