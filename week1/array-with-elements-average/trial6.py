class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1,len(nums)-1):
            if (nums[i-1]+nums[i+1])/2==nums[i]:
                b=nums[i+1]
                nums[i+1]=nums[i]
                nums[i]=b
        for i in range(len(nums)-2,0,-1):
                if (nums[i-1]+nums[i+1])/2==nums[i]:
                    b=nums[i-1]
                    nums[i-1]=nums[i]
                    nums[i]=b
        for i in range(1,len(nums)-1):
            if (nums[i-1]+nums[i+1])/2==nums[i]:
                b=nums[i+1]
                nums[i+1]=nums[i]
                nums[i]=b
        return nums
        
