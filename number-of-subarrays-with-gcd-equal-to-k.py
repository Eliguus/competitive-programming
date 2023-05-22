class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(num1,num2):
            if num2==0:
                return num1
            return gcd(num2,num1%num2)
        ans = 0
        for i, val in enumerate(nums):
            curGcd = val
            
            j = i
            while j<len(nums) and curGcd >= k:
                
                curGcd = gcd(curGcd,nums[j])
                if curGcd==k:
                    ans+=1
                j+=1
        return ans