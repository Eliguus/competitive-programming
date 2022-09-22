class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        m=0
        nums=sorted(nums)
        ans=[]
        for m in range(len(nums)):
            l=m+1
            r=len(nums)-1
            while l<r:
                if nums[l]+nums[m]+nums[r]==0:
                    
                    if  sorted([nums[r],nums[m],nums[l]]) not in ans:
                        ans+=[sorted([nums[l],nums[m],nums[r]])]
                    l+=1
                    r-=1
                elif nums[l]+nums[m]+nums[r]>0:
                    r-=1
                elif nums[l]+nums[m]+nums[r]<0:
                    l+=1
            
        
        return ans
                    
        
