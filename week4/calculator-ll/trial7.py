class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        num=0
        sign='+'
        for ind in range(len(s)):
            if s[ind].isdigit():
                num=num*10+int(s[ind])
            if s[ind] in '/+*-' or ind==len(s)-1:
                if sign=='+':
                    stack.append(num)
                elif sign=='-':
                    stack.append(-num)
                elif sign=='*':
                    stack.append(stack.pop()*num)
                elif sign=='/':
                    stack.append(int(stack.pop()/num))
                num=0
                sign=s[ind]
            if len(stack)>2:
                stack=[sum(stack[:-1]),stack[-1]]
                
                
        return sum(stack)
        
