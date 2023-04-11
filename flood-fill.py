class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()
        initial = image[sr][sc]
        image[sr][sc]=color
        def inside(row,col):
            return (0<=row<len(image) and 0<=col<len(image[0]))
        def dfs(row,col):
            nonlocal color
            nonlocal initial
            for i,j in directions:
                new_col = col+i
                new_row = row+j
                if inside(new_row,new_col) and image[new_row][new_col]==initial and (new_row,new_col) not in visited:
                    visited.add((new_row,new_col))
                    image[new_row][new_col]=color
                    dfs(new_row,new_col)
            return
        dfs(sr,sc)
        return image