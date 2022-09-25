class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        first_fruit=-1
        last_fruit=-1
        last_count=0
        count=0
        ans=0
        for fru in fruits:
            if fru==last_fruit or fru==first_fruit:
                count+=1
            else:
                count=last_count+1
            if fru==last_fruit:
                last_count+=1
            else:
                last_count=1
                first_fruit=last_fruit
                last_fruit=fru
            ans=max(ans,count)
        
        return ans
                
                
                
                
