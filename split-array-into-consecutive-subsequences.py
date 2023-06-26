class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heap = []
        heapq.heapify(heap)

        for num in nums:

            while heap and heap[0][0] + 1 < num:
                n, length = heapq.heappop(heap)
                if length < 3:
                    return False

            if not heap:
                heap.append([num,1])

            else:
                if heap[0][0] == num:
                    heapq.heappush(heap,[num,1])
                else:
                    n,length = heapq.heappop(heap)
                    heapq.heappush(heap,[num,length+1])

        for n,length in heap:
            if length<3:
                return False
        return True