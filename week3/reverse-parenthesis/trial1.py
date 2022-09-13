class Solution:
    def reverseParentheses(self, s: str) -> str:
        ans=[]
        for i in s:
            temp=''
            if i!=')':
                ans=ans+[i]
            else:
                while ans[-1]!='(':
                    temp=temp+ans.pop()
                ans.pop()
            if temp!='':
                for i in temp:
                    ans=ans+[i]
        return ''.join(ans)
                    
        
