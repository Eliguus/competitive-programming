class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[1]*len(nums)
        for idx,num in enumerate(nums):
            ans[idx]=nums[num]
        return ans
