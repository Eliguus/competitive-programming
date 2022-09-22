class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        m=1
        nums=sorted(nums)
        ans=[]
        while m<len(nums)-1:
            l=0
            r=len(nums)-1
            while l<r:
                if l==m:
                    l+=1
                    
                elif r==m:
                    r-=1
                    
                elif nums[l]+nums[m]+nums[r]==0:
                    
                    if [nums[l],nums[m],nums[r]] not in ans and [nums[l],nums[r],nums[m]] not in ans and [nums[m],nums[l],nums[r]] not in ans and [nums[m],nums[r],nums[l]] not in ans and [nums[r],nums[l],nums[m]] not in ans and [nums[r],nums[m],nums[l]] not in ans:
                        ans+=[[nums[l],nums[m],nums[r]]]
                    l+=1
                    r-=1
                elif nums[l]+nums[m]+nums[r]>0:
                    r-=1
                elif nums[l]+nums[m]+nums[r]<0:
                    l+=1
            m+=1
        
        return ans
                    
        
