class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        if '*' or '/' or '+' or '-' not in s:
            return int(s)
        for exp in s:
            if exp==' ':
                continue
            stack.append(exp)
            if len(stack)>=3:
                if stack[-2]=='/':
                    sec=stack.pop()
                    stack.pop()
                    fir=stack.pop()
                    stack.append(str(int(fir)//int(sec)))
                           
            if len(stack)>=3:
                  if stack[-2]=='*':
                    sec=stack.pop()
                    stack.pop()
                    fir=stack.pop()
                    stack.append(str(int(fir)*int(sec)))
            if len(stack)>=3:
                if stack[-2]=='-':
                    num=stack.pop()
                    sign=stack.pop()
                    stack.append(sign+num)
        ans=0
        for num in stack:
            if num!='+':
                ans+=int(num)                 
                                 
        return ans
        
