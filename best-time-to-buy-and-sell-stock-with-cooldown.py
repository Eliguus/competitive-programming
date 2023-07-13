class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dic = {}

        def dp(idx,parity):
            if idx>=len(prices):
                return 0

            if (idx,parity) in dic:
                return dic[(idx,parity)]
            
            if parity:
                temp1 = dp(idx+1,0) - prices[idx]
                temp2 = dp(idx+1,1)

            else:
                temp1 = dp(idx+2,1) + prices[idx]
                temp2 = dp(idx+1,0)
            
            dic[(idx,parity)] = max(temp1,temp2)
            return dic[(idx,parity)]
        return dp(0,1)