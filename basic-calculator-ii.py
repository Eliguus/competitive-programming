class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        operation='+'
        num=''
        s+='+'
        for char in s:
            if char in '0123456789':
                num+=char
            if char in '/+*-':
                if operation=='+':
                    stack.append(int(num))
                elif operation=='-':
                    stack.append(-int(num))
                elif operation=='*':
                    stack.append(stack.pop()*int(num))
                elif operation=='/':
                    stack.append(int(stack.pop()/int(num)))
                num=''
                operation=char
        print(stack)
        return sum(stack)