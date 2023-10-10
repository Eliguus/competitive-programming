class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Dic=Counter(s1)
        s2Dic=defaultdict(int)
        if len(s1)>len(s2):
            return False
        for i in range(len(s1)):
            s2Dic[s2[i]]+=1
        if s1Dic==s2Dic:
            return True
        for idx in range(len(s1),len(s2)):
            s2Dic[s2[idx-len(s1)]]-=1
            s2Dic[s2[idx]]+=1
            if s2Dic[s2[idx-len(s1)]]==0:
                del s2Dic[s2[idx-len(s1)]]
            if s1Dic==s2Dic:
                return True
        return False