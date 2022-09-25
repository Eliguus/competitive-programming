class Solution:
    def compress(self, chars: List[str]) -> int:
        last_char=''
        count=0
        l=[]
        chars+=[0]
        for char in chars:
            if char==last_char:
                count+=1
            else:
                if count==1:
                    l+=[last_char]
                elif 9>=count>1:
                    l+=[last_char,str(count)]
                elif count>9:
                    l+=[last_char]
                    for i in str(count):
                        l+=[i]
                last_char=char
                count=1
        chars[:]=l[:]
        print(l)
        return len(chars)
