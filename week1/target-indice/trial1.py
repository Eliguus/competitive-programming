class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j]>nums[j+1]:
                    b=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=b
        out=[]           
        for i in range(len(nums)):
            if nums[i]==target:
                out=out+[i]
        return out
                
        
