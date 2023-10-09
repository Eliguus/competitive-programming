class Solution:
    def findCheapestPrice(self, n: int, fligts: List[List[int]], src: int, dst: int, k: int) -> int:
        grap = defaultdict(list)
        for srcs,dsts,cost in fligts:
            grap[srcs].append((dsts,cost))
        pat = [(0,src,0)]
        
        heapq.heapify(pat)
        seen=defaultdict(int)
        count=0
        while pat:
            
            cost,node,stops = heapq.heappop(pat)
            seen[node] = stops
            if node == dst and stops <= k+1:
                return cost
            if stops>k:
                continue
            for cild,costs in grap[node]:
                if cild not in seen or seen[cild] > stops:
                    heapq.heappush(pat,(cost+costs,cild,stops+1))
                
        return -1