class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxPair = 0
        curMax = 0
        for idx in range(len(values)):
            maxPair = max(maxPair, curMax + values[idx] - idx)
            curMax = max(curMax, values[idx] + idx)
        
        return maxPair