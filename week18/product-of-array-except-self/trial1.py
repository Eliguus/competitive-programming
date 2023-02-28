class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1 
        post = 1
        arr = [1]*len(nums)
        for idx,num in enumerate(nums):
            
            arr[idx] = pre
            pre *= num
        for idx in range(len(nums)-1,-1,-1):
            arr[idx] *=post
            post *= nums[idx]
            
        return arr
