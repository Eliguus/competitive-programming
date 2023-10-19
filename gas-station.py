class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total = 0
        current = 0
        for i in range(n):
            if current + gas[i] - cost[i] >= 0:
                if current == 0:
                    start = i
                current = current + gas[i] - cost[i]
            else:
                current = 0
            total = total + gas[i] - cost[i]
        if total < 0:
            return -1
        return start