class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        time = {costs[0]:1, costs[1]:7, costs[2]:30}
        n = len(days)
        @lru_cache(None)
        def helper(i, busPass):
            if i == n: return  0
            if busPass >= days[i]: 
                return helper(i + 1, busPass) # skip
            else: 
                return min([cost + helper(i+1, days[i] + time[cost] - 1) for cost in costs])
        return helper(0, 0)