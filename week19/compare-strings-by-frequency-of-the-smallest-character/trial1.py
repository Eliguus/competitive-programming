class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        query = []
        word = []

        for idx,q in enumerate(queries):
            a=Counter(q)
            e=list(a.keys())
            e.sort()
            query.append([a[e[0]],idx])

        for w in words:
            a=Counter(w)
            e=list(a.keys())
            e.sort()
            word.append(a[e[0]])
        query.sort()
        word.sort()
        ans=[0]*len(query)
        ptr=0
        for i,idx in query:
            while ptr<len(word) and i>=word[ptr]:
                ptr+=1
            ans[idx]=len(word)-ptr

        return ans
