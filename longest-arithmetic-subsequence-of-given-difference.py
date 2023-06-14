class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        ans = 1
        for num in arr:
            pre = dp.get(num-difference,0)
            dp[num] = pre+1
            ans = max(ans,dp[num])
        return ans