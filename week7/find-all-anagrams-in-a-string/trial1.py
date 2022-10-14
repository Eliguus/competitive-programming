class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left=0
        right=0
        pmap=Counter(p)
        dist=len(pmap)
        ans=[]
        while right<len(s):
            if s[right] in pmap:
                pmap[s[right]]-=1
                if pmap[s[right]]==0:
                    dist-=1
            if right-left+1<len(p):
                right+=1
            else:
                if dist==0:
                    ans+=[left]
                if s[left] in pmap:
                    pmap[s[left]]+=1
                    if pmap[s[left]]==1:
                        dist+=1
                left+=1
                right+=1
        return ans
