class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        seen={}
        for winner,loser in matches:
            seen[winner]=seen.get(winner,0)
            seen[loser]=seen.get(loser,0)+1
        answer=[[],[]]
        for val,count in seen.items():
            if count==0:
                answer[0]+=[val]
            elif count==1:
                answer[1]+=[val]
        answer[0]=sorted(answer[0])
        answer[1]=sorted(answer[1])
        return answer
