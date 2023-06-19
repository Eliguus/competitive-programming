class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        size = len(points)
        h = []
        for i in range(1, size):
            heapq.heappush(h,(abs(points[i][0] - points[0][0]) + abs(points[i][1] - points[0][1]),i,),)

        result = 0
        c = 0
        candidates = {i for i in range(1, size)}
        while len(h) > 0 and c < size:
            dis, cur = heapq.heappop(h)
            if cur not in candidates:
                continue
            candidates.remove(cur)
            result += dis
            c += 1
            for i in candidates:
                heapq.heappush(h,(abs(points[i][0] - points[cur][0]) + abs(points[i][1] - points[cur][1]),i,),)

        return result