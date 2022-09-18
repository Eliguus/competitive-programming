class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        length=2*len(pushed)
        for i in range(length):
            if pushed:
                stack.append(pushed[0])
                pushed.pop(0)
            if  popped:
                while stack[-1]==popped[0]:
                    stack.pop()
                    popped.pop(0)
                    if not stack:
                        break
        
        if len(stack)==0:
            return True
        return False
