class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def flip(n,k):
            if n==0:
                return 0

            if k%2:
                return 1-flip(n-1,k//2)
            else:
                return flip(n-1,k//2)

        return flip(n-1,k-1)
