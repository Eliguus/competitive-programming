class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        c_arr=[]
        for i in range(len(nums)):
            count=0
            
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    count=count+1
            c_arr=c_arr+[count]
        return c_arr
        
