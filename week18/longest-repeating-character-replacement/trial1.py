class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        l=0
        mf=0
        ans=0
        for r in range(len(s)):
            d[s[r]]=d.get(s[r],0)+1
            mf=max(mf,d[s[r]])
            if r-l-mf+1>k:
                d[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans
        
        
        
        sd=Counter(s)
        m=0
        for i in sd.keys():
            l=0
            c=0
            for j in range(len(s)):
                if s[j]==i:
                    c+=1
                while j-c-l+1>k:
                    if s[l]==i:
                        c-=1
                    l+=1
                m=max(m,j-l+1)
        return m
