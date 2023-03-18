class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def dfs(cur, cur_sum, idx):                       
            if cur_sum > target: 
                return                   
            if cur_sum == target: 
                ans.append(cur)
                return 
            for i in range(idx, n): 
                dfs(cur + [candidates[i]], cur_sum + candidates[i], i) 
        dfs([], 0, 0)
        return ans        
