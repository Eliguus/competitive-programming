class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_even=0
        for num in nums:
            if num%2==0:
                sum_even+=num
        ans=[]
        for val,idx in queries:
            if nums[idx]%2==0:
                sum_even-=nums[idx]
            nums[idx]+=val
            if (nums[idx])%2==0:
                sum_even+=nums[idx]
            ans.append(sum_even)
        return ans
