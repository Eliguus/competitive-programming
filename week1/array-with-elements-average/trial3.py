class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for j in range(len(nums)//2):
            for i in range(1,len(nums)-1):
                if (nums[i-1]+nums[i+1])/2==nums[i]:
                    b=nums[i+1]
                    nums[i+1]=nums[i]
                    nums[i]=b
        return nums
        
