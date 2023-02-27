class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sDic = Counter(s[:len(p)])
        pDic = Counter(p)
        indices = []

        if sDic==pDic:
            indices.append(0)

        for idx in range(len(p),len(s)):
            sDic[s[idx-len(p)]]-=1
            sDic[s[idx]]+=1
            if sDic[s[idx-len(p)]]==0:
                del sDic[s[idx-len(p)]]
            if sDic==pDic:
                indices.append(idx-len(p)+1)
        return indices
