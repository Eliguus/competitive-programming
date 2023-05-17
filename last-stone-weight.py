class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone = [-s for s in stones]
        heapq.heapify(stone)
        
        while len(stone)>1:
            a = -heapq.heappop(stone)
            s = -heapq.heappop(stone)
            if a>s:
                heapq.heappush(stone,s-a)
        
        return -stone[0] if len(stone) else 0