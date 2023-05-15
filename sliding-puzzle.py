class Solution:
    def slidingPuzzle(self, puzzle: List[List[int]]) -> int:
        temp = []
        for num in range(1,6):
            temp.append(num)
        temp.append(0)
        ans = tuple(temp)
        
        cur = tuple(puzzle[0]+puzzle[1])
        
        if cur==ans:
            return 0

        canSwap = {0:[1,3],1:[0,2,4],2:[1,5],3:[0,4],4:[3,1,5],5:[2,4]}
        visited = set()
        
        def swap(puzzles,idx_zero,idx_swap):
            puzzles[idx_zero],puzzles[idx_swap] = puzzles[idx_swap],puzzles[idx_zero]
            
            return tuple(puzzles)

        def find_zero(inputs):
            puzzles = list(inputs)
            for i in range(6):
                if not puzzles[i]:
                    return i
        queue=deque()
        queue.append(cur)
        moves = 0
        while queue:
            newQueue = deque()

            while queue:
                curPuzzle = queue.popleft()
                
                if curPuzzle == ans:
                    return moves
                
                zero_idx = find_zero(curPuzzle)
                
                for i in canSwap[zero_idx]:
                    
                    curP = list(curPuzzle)
                    temp=swap(curP,zero_idx,i)
                    
                    if temp not in visited:
                        
                        newQueue.append(temp)
                        visited.add(temp)
            
            queue=newQueue
           
            moves+=1
        return -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        queue = deque()

        steps = 0

        ans = [[1,2,3],[4,5,0]]
        if ans == boards:
            return 0

        zero = [0,0]
        for i in range(2):
            for j in range(3):
                if not boards[i][j]:
                    zero = [i,j]
        print(zero)
        visited = set()
        def test(zero,board,queue=[]):
            oard=[]
            if zero[1]==0 and zero[0]==0:
                
                board[0][0],board[0][1]=board[0][1],board[0][0]
                if str(board) not in visited:
                    oard=board[:]
                    queue.append(oard)
                    visited.add(str(oard))
    
                board[0][0],board[0][1]=board[0][1],board[0][0]
                board[0][0],board[1][0]=board[1][0],board[0][0]
                if str(board) not in visited:
                    oard=board[:]
                    queue.append(oard)
                    visited.add(str(oard))
                board[0][0],board[1][0]=board[1][0],board[0][0]
                
            elif zero[1]==1 and zero[0]==0:
                board[0][0],board[0][1]=board[0][1],board[0][0]
                if str(board) not in visited:
                    oard=board[:]
                    queue.append(oard)
                    visited.add(str(oard))
    
                board[0][0],board[0][1]=board[0][1],board[0][0]
                board[0][1],board[1][0]=board[1][0],board[0][1]
                if str(board) not in visited:
                    oard=board[:]
                    queue.append(oard)
                    visited.add(str(oard))
    
                board[0][1],board[1][0]=board[1][0],board[0][1]
                board[0][2],board[0][1]=board[1][0],board[0][2]
                if str(board) not in visited:
                    oard=board[:]
                    queue.append(oard)
                    visited.add(str(oard))
    
                board[0][2],board[0][1]=board[0][1],board[0][2]
            elif zero[1]==2 and zero[0]==0:
                board[0][2],board[0][1]=board[0][1],board[0][2]
                if str(board) not in visited:
                    oard=board[:]
                    queue.append(oard)
                    visited.add(str(oard))
    
                board[0][2],board[0][1]=board[0][1],board[0][2]
                board[0][2],board[1][2]=board[1][2],board[0][2]
                if str(board) not in visited:
                    oard=board[:]
                    queue.append(oard)
                    visited.add(str(oard))
    
                board[0][2],board[1][2]=board[1][2],board[0][2]
            elif zero[1]==0 and zero[0]==1:
                board[1][0],board[1][2]=board[1][2],board[1][0]
                if str(board) not in visited:
                    oard=board[:]
                    queue.append(oard)
                    visited.add(str(oard))
    
                board[1][0],board[1][2]=board[1][2],board[1][0]
                board[0][0],board[1][0]=board[1][0],board[0][0]
                if str(board) not in visited:
                    oard=board[:]
                    queue.append(oard)
                    visited.add(str(oard))
    
                board[0][0],board[1][0]=board[1][0],board[0][0]
            elif zero[1]==1 and zero[0]==1:
                board[1][0],board[1][1]=board[1][1],board[1][0]
                
                if str(board) not in visited:
                    oard=board[:]
                    print(oard)
                    queue.append(oard)
                    print(queue)
                    print(oard)
                    visited.add(str(oard))
                print(queue)
                board[1][0],board[1][1]=board[1][1],board[1][0]
                print(queue)
                board[0][1],board[1][1]=board[1][1],board[0][1]
                if str(board) not in visited:
                    oard=board[:]
                    queue.append(oard)
                    visited.add(str(oard))
                    
    
                board[0][1],board[1][1]=board[1][1],board[0][1]
                board[1][2],board[1][1]=board[1][1],board[1][2]
                if str(board) not in visited:
                    oard=board[:]
                    queue.append(oard)
                    visited.add(str(oard))
                board[1][2],board[1][1]=board[1][1],board[1][2]
                
            elif zero[1]==2 and zero[0]==1:
                board[1][2],board[1][1]=board[1][1],board[1][2]
                if str(board) not in visited:
                    oard=board[:]
                    queue.append(oard)
                    visited.add(str(oard))
    
                board[1][2],board[1][1]=board[1][1],board[1][2]
                board[1][2],board[0][2]=board[0][2],board[1][2]
                if str(board) not in visited:
                    oard=board[:]
                    queue.append(oard)
                    visited.add(str(oard))
    
                board[1][2],board[0][2]=board[0][2],board[1][2]

            
            return queue
        aa=boards[:]
        queue = test(zero,aa,[])
        if str(ans) in visited:
            return 1
        while queue:

            newQueue = []
            
            while queue:
                temp = list(queue.pop(0))
                print(queue)
                if temp==ans:
                    return steps
                for i in range(2):
                    for j in range(3):
                        
                        if not temp[i][j]:
                            zero = [i,j]
                if str(temp) not in visited:
                    newQueue.extend(test(zero,temp,[]))
                    
            steps+=1
            queue = newQueue[:]
        return -1