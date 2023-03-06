class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        mid = l+(r-l)//2
        while l<=r:
            mid = l+(r-l)//2

            if nums[mid]>target:
                r=mid-1
            
            elif nums[mid]<target:
                l=mid+1

            else:
                break
        
        if not nums or nums[mid]!=target:
            return [-1,-1]
        l=mid
        while l>=0 and nums[l]==target:
            l-=1
        r=mid  
        while r<len(nums) and nums[r]==target:
            r+=1

        return [l+1,r-1]
