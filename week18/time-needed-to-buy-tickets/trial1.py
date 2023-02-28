class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time=0
        while True:
            for idx in range(len(tickets)):
                
                if tickets[idx]>0:
                    tickets[idx]-=1
                    time+=1
                if tickets[k]==0:
                    return time
