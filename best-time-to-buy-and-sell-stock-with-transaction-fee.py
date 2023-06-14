class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        p = 0
        h = -prices[0]

        for i in range(1,len(prices)):
            tmp = h
            h = max(h,p-prices[i])
            p = max(p,tmp+prices[i]-fee)

        return p