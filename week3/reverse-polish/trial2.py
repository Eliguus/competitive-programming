class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans=[]
        
        for i in tokens:
            if i=='+':
                ans.append(ans.pop() + ans.pop())
                
            elif i=='-':
                var1=ans.pop()
                var2=ans.pop()
                ans.append(var2 - var1)
                
            elif i=='*':
                var1=ans.pop()
                var2=ans.pop()
                ans.append(var2 * var1)
                
            elif i=='/':
                var1=ans.pop()
                var2=ans.pop()
                
                ans.append(int(var2/var1))
                
            else:
                ans.append(int(i))
            
            
                
        return ans[0]
            
        
