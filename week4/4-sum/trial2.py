class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        nums=sorted(nums)
        for first in range(len(nums)):
            last=len(nums)-1
            while last>first:
                l=first+1
                r=last-1
                while l<r and first<last:
                    if nums[l]+nums[r]+nums[first]+nums[last]==target:
                        if sorted([nums[l],nums[r],nums[first],nums[last]]) not in ans:
                            ans+=[[nums[l],nums[r],nums[first],nums[last]]]
                        l+=1
                        r-=1
                    elif nums[l]+nums[r]+nums[first]+nums[last]<target:
                        l+=1
                    else:
                        r-=1
                last-=1
        return ans
        
