class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        def inside(row,col):
            return ((0<=row<len(grid)) and (0<=col<len(grid)))
        def dfs(row,col):
            visited.add((row,col))
            queue.append((row,col))
            for i,j in direction:
                if inside(row+i,col+j) and (row+i,col+j) not in visited and grid[row+i][col+j]:
                    visited.add((row+i,col+j))
                    queue.append((row+i,col+j))
                    dfs(row+i,col+j)
        place = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j]:
                    place.append([i,j])
        dfs(place[0][0],place[0][1])
        distance = 0
        while queue:
            newQueue = deque()
            while queue:
                x,y = queue.popleft()
                for i,j in direction:
                    if inside(x+i,y+j) and grid[x+i][y+j]==0 and (x+i,y+j) not in visited:
                        visited.add((x+i,y+j))
                        newQueue.append((x+i,y+j))
                    if inside(x+i,y+j) and grid[x+i][y+j] and (x+i,y+j) not in visited:
                        return distance
            distance+=1
            queue = newQueue