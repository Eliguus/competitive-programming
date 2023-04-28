class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(0,1),(-1,0),(0,-1),(1,0)]
        def inside(row,col):
            return ((0<=row<len(mat)) and (0<=col<len(mat[0])))
        


        queue = deque()
        ans = [[10**8]*len(mat[0]) for i in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    queue.append((i,j))
                    ans[i][j]=0
        
        
        
        
        while queue:
            r,c = queue.popleft()
            #visited.add((r,c))
            for i,j in directions:
                if inside(i+r,j+c) and ans[i+r][j+c]>ans[r][c]:
                    ans[i+r][j+c]=ans[r][c]+1
                    queue.append((i+r,j+c))
                    #visited.add((i+r,j+c))
                

        

        
        return ans