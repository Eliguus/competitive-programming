class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dic = [set() for i in range(26)]
        for idx in range(len(s1)):
            i = 0
            while len(dic[i]) and (s1[idx] not in dic[i] and s2[idx] not in dic[i]):
                i+=1
            dic[i].add(s1[idx])
            dic[i].add(s2[idx])
        ans = []
        for idx in range(26):
            i = 0
            for i in range(idx,26):
                for letter in list(dic[idx]):
                    if letter in dic[i]:
                        dic[i].update(dic[idx])
                        dic[idx].update(dic[i])
        for letter in baseStr:
            i = 0
            while i<26 and letter not in dic[i]:
                i+=1
            if i==26:
                ans.append(letter)
            else:
                ans.append(min(dic[i]))
        
        return ''.join(ans)