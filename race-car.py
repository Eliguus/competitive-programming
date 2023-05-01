class Solution:
    def racecar(self, target: int) -> int:
        queue = deque()
        queue.append((0,1))
        steps = 0
        while queue:
            newQueue = deque()
            while queue:
                pos,speed = queue.popleft()
                if pos == target:
                    return steps
                newQueue.append((pos+speed,speed*2))

                if speed>0:
                    reverse = -1

                else:
                    reverse = 1

                if ((pos+speed)<target and speed<0) or ((pos+speed)>target and speed>0):
                    newQueue.append((pos,reverse))
            queue = newQueue
            steps+=1