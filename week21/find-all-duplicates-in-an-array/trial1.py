class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ptr=0
        arr=[]
        while ptr<len(nums):
            if nums[ptr]-1==ptr:
                ptr+=1

            else:
                if nums[nums[ptr]-1]==nums[ptr]:
                    if nums[ptr] not in arr:
                        arr.append(nums[ptr])
                    ptr+=1
                else:
                    nums[nums[ptr]-1],nums[ptr]=nums[ptr],nums[nums[ptr]-1]

        return arr
