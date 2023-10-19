class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n, memo = len(nums), {}
        def not_yet_selected(i, j, mask):
            return not ((1 << i) & mask or (1 << j) & mask)

        def dfs(operations, mask):
            if operations > n//2: return 0
            if (operations, mask) in memo: return memo[(operations, mask)]
            ans = 0
            for i in range(n):
                for j in range(i+1,n):
                    if not_yet_selected(i, j, mask):
                        
                        updated = (mask | 1<<i | 1<<j)
                        ans = max(ans, operations * gcd(nums[i], nums[j]) + dfs(operations + 1, updated))
            memo[(operations, mask)] = ans
            return ans
        
        return dfs(1, 0)