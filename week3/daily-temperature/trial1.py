class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days=[]
        for i in range(len(temperatures)):
            count=0
            for j in range(i+1,len(temperatures)):
                count+=1
                if temperatures[i]<temperatures[j]:
                    days=days+[count]
                    break
                if count==len(temperatures)-i-1:
                    days=days+[0]
                    break
        days=days+[0]
        return days
                    
                    
                
                
                
        
