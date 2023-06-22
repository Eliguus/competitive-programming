class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        res = []
        heap = []
        visited = set()
        heapq.heappush(heap, (nums1[0]+nums2[0], 0, 0))
        visited.add((0, 0))

        while heap and len(res) < k:
            su, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])

            if i+1 < min(k, len(nums1)) and (i+1, j) not in visited:
                visited.add((i+1, j))
                heapq.heappush(heap, (nums1[i+1]+nums2[j], i+1, j))
            if j+1 < min(k, len(nums2)) and (i, j+1) not in visited:
                visited.add((i, j+1))
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
        return res