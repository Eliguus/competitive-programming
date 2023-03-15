class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def calculate(n,k):
            if n==1:
                return 0

            if k==2**(n-1):
                return 1
            elif k>2**(n-1):
                return 1-calculate(n-1,2**n-k)
            else:
                return calculate(n-1,k)

        return str(calculate(n,k))
