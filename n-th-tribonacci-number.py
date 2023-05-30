class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def tri(n):
            if n==0:
                return 0

            elif n==1 or n==2:
                return 1
            if n not in memo:
                memo[n] = tri(n-1)+tri(n-2)+tri(n-3)
            return memo[n]
        return tri(n)