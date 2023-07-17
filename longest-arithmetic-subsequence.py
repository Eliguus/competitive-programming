class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        ans = 0
        for right in range(len(nums)):
            for left in range(right):
                dif = nums[right] - nums[left]
                if not dic[(left,dif)]:
                    dic[(left,dif)] +=1
                dic[(right,dif)] = dic[(left,dif)] + 1
                ans = max(ans,dic[(right,dif)])
        return ans