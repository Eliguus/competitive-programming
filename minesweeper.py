class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(1,0),(-1,0),(0,-1)]

        if board[click[0]][click[1]]=='M':
            board[click[0]][click[1]]='X'
            return  board
        def inside(row,col):
            return (0<=row<len(board)) and (0<=col<len(board[0]))

        def dfs(r,c):
            if board[r][c] != 'E':
                return

            count = 0
            for x,y in directions:
                dx = x+r
                dy = y+c
                if inside(dx,dy) and board[dx][dy] == 'M':
                    count+=1
            if count:
                board[r][c] = str(count)
                return 
            board[r][c] = 'B'
            for x,y in directions:
                dx = x+r
                dy = y+c
                if inside(dx,dy):
                    dfs(dx,dy)
        dfs(click[0],click[1])
        return board