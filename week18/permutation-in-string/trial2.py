class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=[*s1]
        s2=[*s2]
        s1.sort()
        for idx in range(len(s2)-len(s1)+1):
            temp=sorted(s2[idx:idx+len(s1)])
            if s1==temp:
                return True
        return False
