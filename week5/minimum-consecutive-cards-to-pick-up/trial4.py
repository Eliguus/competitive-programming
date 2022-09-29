class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dc={}
        count=0
        ans=len(cards)+1
        for card in cards:
            if card in dc:
                ans=min(ans,count-dc[card]+1)
            dc[card]=count
            count+=1 
        if ans==len(cards)+1:
            return -1 
        else:
            return ans
        
            
        
