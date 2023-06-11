class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def tracking(arr):
            
            if len(arr)==len(nums):
                ans.append(arr[:])
                return
            for num in nums:
                if num not in arr:
                    arr.append(num)
                    tracking(arr)
                    arr.pop()
            
            return
        for num in nums:
            tracking([num])
        
        return ans