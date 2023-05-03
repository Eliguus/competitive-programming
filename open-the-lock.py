class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque()
        queue.append('0000')
        moves = 0
        visited = set()
        for i in deadends:
            visited.add(i)
        while queue:
            newQueue = deque()

            while queue:
                some = queue.popleft()
                com = [*some]
                #print(queue)
                
                
                
                
                if some not in visited:
                    visited.add(some)
                    if some == target:
                        return moves
                    for i in range(8):
                        temp = com.copy()
                        #print(temp)
                        # if int(temp[i])==9:
                        #     continue
                        if i>=4:
                            if temp[i%4]=='9':
                                temp[i%4]='0'
                            else:
                                temp[i%4]=str(int(temp[i%4])+1)
                        else:
                            if temp[i]=='0':
                                temp[i]='9'
                            else:
                                temp[i]=str(int(temp[i])-1)
                        a = ''.join(temp)
                        
                        if (a not in visited) and (a not in deadends):
                            
                            newQueue.append(a)
                            
            queue = newQueue
            moves+=1
        return -1