class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = defaultdict(int)
        def tracking(idx,path):
            ans[path]+=1

            for i in range(idx+1,len(nums)):
                tracking(i,path|nums[i])
        tracking(-1,0)
        res = max(ans.values())

        return res