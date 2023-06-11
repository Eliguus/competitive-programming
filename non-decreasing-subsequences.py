class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def backtrack(idx,path):
            if len(path) >= 2: res.add(tuple(path))

            for i in range(idx,n):
                if path == [] or path[-1] <= nums[i]:
                    backtrack(i+1,path+[nums[i]])

        res = set()
        backtrack(0,[])
        return res