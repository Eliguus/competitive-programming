class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        
        dic = {}
        def dp(idx,time):
            if idx >= len(satisfaction):
                return 0

            if (idx,time) in dic:
                return dic[(idx,time)]

            temp1 = (time * satisfaction[idx]) + dp(idx+1,time+1)
            temp2 = dp(idx+1,time)

            dic[(idx,time)] = max(temp1,temp2)
            return dic[(idx,time)]
        
        return dp(0,1)