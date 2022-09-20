class Solution:
    def calculate(self, s: str) -> int:
        red=''
        for val in s:
            if val==' ':
                continue
            red+=val
            if len(red)>=3:
                if red[-2]=='/':
                    temp=int(red[-3])//int(val)
                    red=red[:len(red)-3]
                    red+=str(temp)
            if len(red)>=3:    
                if red[-2]=='*':
                    temp=int(red[-3])*int(val)
                    red=red[:len(red)-3]
                    red+=str(temp)
        ans=''
        for val in red:
            ans+=val
            if len(ans)>=3:
                if ans[-2]=='+':
                    temp=int(ans[-3])+int(val)
                    ans=ans[:len(ans)-3]
                    ans+=str(temp)
            if len(ans)>=3:        
                if ans[-2]=='-':
                    temp=int(ans[-3])-int(val)
                    ans=ans[:len(ans)-3]
                    ans+=str(temp)
        return int(ans)
        
