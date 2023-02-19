class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        p=sorted(players)
        t=sorted(trainers)
        p1=len(p)-1
        t1=len(t)-1
        c=0
        for i in range(len(p)):
            if t1>-1 and p[p1]<=t[t1]:
                c+=1
                p1-=1   
                t1-=1
            else:
                p1-=1
        return c
        
        p=sorted(players)
        t=sorted(trainers)
        p1=len(p)-1
        t1=len(t)-1
        c=0
        while p1>=0 and t1>=0:
            if p[p1]<=t[t1]:
                c+=1
                p1-=1   
                t1-=1
            else:
                p1-=1
        return c
