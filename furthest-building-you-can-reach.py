class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        diffArray = []
        heapq.heapify(diffArray)

        for i in range(1,len(heights)):
            dif = heights[i] - heights[i-1]

            if dif > 0:
                if bricks >= dif:
                    bricks -= dif
                    heapq.heappush(diffArray, -dif)
                
                elif ladders > 0:
                    if diffArray and dif < -diffArray[0]:
                        bricks += -heapq.heappop(diffArray) - dif
                        heapq.heappush(diffArray, -dif)
                    ladders-=1
                else:
                    return i-1
        return len(heights)-1