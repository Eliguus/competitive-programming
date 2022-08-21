class Solution:
    def sortSentence(self, s: str) -> str:
        list=s.split()
        for i in range(len(list)):
            
            for j in range(len(list)-1):
                
                if list[j][-1]>list[j+1][-1]:
                    d=list[j]
                    list[j]=list[j+1]
                    list[j+1]=d
        s=''            
        for i in range(len(list)):
            s=s+((list[i][:len(list[i])-1]))+' '
        s=s[:len(s)-1]
        return s
        
