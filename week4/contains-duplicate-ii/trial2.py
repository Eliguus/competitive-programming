class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length=len(nums)
        nums=enumerate(nums)
        order=[]
        for i,j in nums:
            order+=[[j,i]]
        order=sorted(order)
        l=0
        r=1
        
        while  r<length:
            if order[r][0]==order[l][0] and abs(order[r][1]-order[l][1])<=k:
                return True
            else:
                r+=1
                l+=1
        return False
            
                    
        
