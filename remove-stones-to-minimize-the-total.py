class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        arr = [-i for i in piles]
        heapq.heapify(arr)

        for _ in range(k):
            temp = -heapq.heappop(arr)
            heapq.heappush(arr,-temp+temp//2)

        return -sum(arr)