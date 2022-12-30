class Solution:
    def similarPairs(self, words: List[str]) -> int:
        hashs=[]
        for word in words:
            h=list(set(word))
            h.sort()
            hashs.append(str(h))
        hash=Counter(hashs)
        pair=0
        for i in hash.values():
            pair+=int(i-1)*int(i)//2
        return pair
