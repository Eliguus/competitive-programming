class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        stack=[i for i in range(n,0,-1)]

        while len(stack)!=1:
            for i in range(1,k):
                
                stack.insert(0,stack.pop())
            stack.pop()
        return stack[0]
        
        
