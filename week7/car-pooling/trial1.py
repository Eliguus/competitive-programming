class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        temp=[0]*1001
        for passa,fromi,to in trips:
            temp[fromi]+=passa
            temp[to]-=passa
        count=0
        for num in temp:
            count+=num
            if count>capacity:
                return False
        return True
