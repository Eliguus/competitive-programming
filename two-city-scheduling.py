class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sums = 0
        costs=sorted(costs,key=lambda x: x[1]-x[0])
    
        for i in range(len(costs)//2):
            sums+=costs[i][1]
        for i in range(len(costs)//2,len(costs)):
            sums+=costs[i][0]
        return sums