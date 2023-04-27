class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        start = (0,0)
        directions = [(0,1),(1,0),(1,1),(1,-1),(-1,1),(-1,0),(0,-1),(-1,-1)]
        visited = set()
        count=1
        if grid[0][0]==1:
            return -1

        queue = deque()
        queue.append((0,0))
        def inside(row,col):
            return ((0<=row<len(grid)) and (0<=col<len(grid[0])))

        while queue:
            newQueue = deque()

            while queue:
                dire = queue.popleft()
                visited.add(dire)

                for i,j in directions:
                    x,y = dire
                    if i+x==len(grid) and j+y==len(grid):
                        return count
                    if inside(x+i,y+j) and (x+i,y+j) not in visited and grid[x+i][y+j]==0:
                        visited.add((x+i,y+j))
                        newQueue.append((x+i,y+j))

            queue = newQueue
            count+=1
        return -1