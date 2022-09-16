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
            if len(stack)==1 and num[i]=='0':
                stack.pop()
            
        if k>0 and stack:
            for i in range(k):
                stack.pop()
        
        if len(stack)==0:
            return '0'
            
                
            
        return ''.join(stack)
            
        
