class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer=0
        count=0
        while pointer<len(nums)-1:
            if nums[pointer]==nums[pointer+1]:
                nums[pointer]=101
                count+=1
            pointer+=1
        holder=0
        seeker=0
        while seeker<len(nums):
            if nums[seeker]!=101:
                nums[seeker],nums[holder]=nums[holder],nums[seeker]
                holder+=1
            seeker+=1
        return len(nums)-count
