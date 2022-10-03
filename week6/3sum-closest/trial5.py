class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans=0
        mindif=10001
        nums.sort()
        for p in range(len(nums)-1):
            l=p+1
            r=len(nums)-1
            while l<r:
                summ=nums[p]+nums[l]+nums[r]
                if abs(summ-target)<mindif:
                    mindif=abs(summ-target)
                    ans=summ
                if summ>target:
                    r-=1
                elif summ<target:
                    l+=1
                else:
                    return target
        
        
        return ans
        
