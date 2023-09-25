class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        team = []
        for age,score in zip(ages,scores):
            team.append([age,score])
        team.sort()
        memo = {}
        print(team)
        def dp(pre,idx):
            if idx >= len(scores):
                return 0
            cur = 0
            if (pre,idx) in memo:
                return memo[(pre,idx)]
            
            if pre==-1 or (team[pre][0] <= team[idx][0] and team[pre][1] <= team[idx][1]):
                cur = team[idx][1] + dp(idx,idx+1)
            
            
            maxi = dp(pre,idx+1)
            maxim = max(maxi,cur)
            memo[(pre,idx)] = maxim
            return maxim
        return dp(-1,0)