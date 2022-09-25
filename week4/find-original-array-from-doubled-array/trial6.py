class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2!=0:
            return []
        changed.sort()
        l=0
        r=1
        ans=[]
        while l<len(changed)-1 and r<len(changed) and r!=l:
            while r<=l:
                r+=1
            
            while changed[l]*2!=changed[r] and r<len(changed)-1:
                r+=1
            if changed[l]*2==changed[r] and l!=r:
                ans+=[changed[l]]
            changed[r]=-1
            if l<len(changed)-1:
                l+=1
            while changed[l]==-1 and l<len(changed)-1:
                l+=1
            
        if len(ans)==len(changed)/2:
            return ans
        return []
    #[0,1,0,0]
    #l,,-1
