class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2!=0:
            return []
        changed.sort()
        l=0
        r=1
        ans=[]
        while l<len(changed)-1 and r<len(changed):
            while changed[l]*2!=changed[r] and r<len(changed)-1:
                r+=1
            if changed[l]*2==changed[r]:
                ans+=[changed[l]]
                changed[r]=-1
            if l<len(changed)-1:
                l+=1
            while changed[l]==-1 and l<len(changed)-1:
                l+=1
            
        if len(ans)==len(changed)/2:
            return ans
        return []
    #[1,2,3,4,6,8]
    #l,-1,l,l,-1,-1
