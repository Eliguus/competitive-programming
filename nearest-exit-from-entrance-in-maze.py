class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        direction = [(1,0),(0,1),(0,-1),(-1,0)]

        def inside(row,col):
            return ((0<=row<len(maze)) and (0<=col<len(maze[0])))
        entrance.append(0)
        visited=set()
        queue = deque()
        queue.append(entrance)
        
        
        while queue:
            x,y,count = queue.popleft()
            maze[x][y]='+'
            for i,j in direction:
                if inside(i+x,j+y) and maze[i+x][j+y]=='.':
                    queue.append([i+x,j+y,count+1])
                    maze[i+x][j+y]='+'
                    if (i+x==0 or i+x==len(maze)-1 or j+y==0 or j+y==len(maze[0])-1):
                        return count+1

             
            
        return -1