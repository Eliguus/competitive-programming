class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)==k:
            return '0'
        
        stack=[]
        for i in range(len(num)):
            
            while k>0 and stack and num[i]<stack[-1]:
                k-=1
                stack.pop()
            stack.append(num[i])
            
        if k>0:
            for i in range(k):
                stack.pop()
        if stack[0]=='0' and len(stack)>1:
            while stack[0]=='0':
                stack.pop(0)
            
                
            
        return ''.join(stack)
            
        
