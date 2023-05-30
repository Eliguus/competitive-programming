class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        
        def minCost(n):
            
            if n==0:
                return cost[0]

            elif n==1:
                return cost[1]
            

            if n not in memo:
                if n==len(cost):

                    memo[n] = min(minCost(n-1),minCost(n-2))
                else:
                    memo[n] = cost[n]+min(minCost(n-1),minCost(n-2))
            return memo[n]
        
        return minCost(len(cost))