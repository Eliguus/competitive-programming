class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board) 
        cols = len(board[0])
        
        def dfs(i,j):
            if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] == "X" or board[i][j] =="g":
                return 
            
            board[i][j] = "g"
            
            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)
            
       #first iterating through the border to turn all invalid O to g or any value  that help u to know that O isnt valid
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i == 0 or j == 0 or i == rows - 1 or j == cols - 1):
                    dfs(i,j)
       #turning all invalid O that we turned it before to g into O again and all other valid O to X
        for i in range(rows):
            for j in range(cols):
                
                if board[i][j] == "g":
                     board[i][j] = "O"
                
                elif board[i][j] == "O":
                    board[i][j] = "X"