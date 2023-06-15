class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        temp = []

        for row in matrix:
            for elem in row:
                temp.append(-elem)
        
        heapq.heapify(temp)
        
        while len(temp)!=k:
            heapq.heappop(temp)
        return -heapq.heappop(temp)