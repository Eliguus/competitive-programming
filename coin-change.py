class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def trac(sums):
            ans = 2**32
            if sums in memo:
                return memo[sums]

            if sums<0:
                return ans
            if sums==0:
                return 0
            for coin in coins:
                ans = min(ans,trac(sums-coin)+1)
            memo[sums]=ans
            return ans
        res = trac(amount)
        if res == 2**32:
            return -1
        return res