class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        string1=list(s)
        string2=list(t)
        string1.sort()
        string2.sort()
        for index,letter in enumerate(string1):
            if letter!=string2[index]:
                return string2[index]
        return string2[-1]
