class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}
        def dp(idx1,idx2):
            if idx1>= len(nums1) or idx2 >= len(nums2):
                return 0
            if (idx1,idx2) in memo:
                return memo[(idx1,idx2)]
            temp1=0
            if nums1[idx1] == nums2[idx2]:
                temp1 = 1 + dp(idx1+1,idx2+1)
            temp2 = dp(idx1+1,idx2)
            temp3 = dp(idx1,idx2+1)
            memo[(idx1,idx2)] = max(temp1,temp2,temp3)
            return memo[(idx1,idx2)]
        return dp(0,0)