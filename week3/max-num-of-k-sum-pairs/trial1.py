class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        List=sorted(nums)
        l=0
        r=len(nums)-1
        count=0
        while l<r:
            if List[l]+List[r]==k:
                l+=1
                r-=1
                count+=1
            elif List[l]+List[r]>k:
                l+=1
            else:
                r-=1
        return count
