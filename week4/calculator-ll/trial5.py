class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        temp=''
        for char in s:
            if char==' ':
                continue
            if char in '/*+-':
                stack.append(int(temp))
                temp=''
                stack.append(char)
            else:
                temp+=char
        stack.append(int(temp))
        stack=stack[::-1]
        ind=1
        while ind<len(stack):
            if stack[ind] =='/':
                first=stack[ind-1]
                sec=stack[ind+1]
                res=sec//first
                stack.pop(ind-1)
                stack.pop(ind-1)
                stack.pop(ind-1)
                stack.insert(ind-1,res)
                ind=ind-1
            elif stack[ind] =='*':
                first=stack[ind-1]
                sec=stack[ind+1]
                res=first*sec
                stack.pop(ind-1)
                stack.pop(ind-1)
                stack.pop(ind-1)
                stack.insert(ind-1,res)
                ind=ind-1
            elif stack[ind]=='-':
                stack.pop(ind)
                val=stack.pop(ind-1)
                stack.insert(ind,-val)
            
            ind+=1
        ans=0
        for num in stack:
            if num!='+':
                ans+=num
                
        return ans
        
