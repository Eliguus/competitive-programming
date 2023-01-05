class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        rearranged=[1]*len(nums)
        idx_neg=1
        idx_pos=0
        for num in nums:
            if num>0:
                rearranged[idx_pos]=num
                idx_pos+=2
            else:
                rearranged[idx_neg]=num
                idx_neg+=2
        return rearranged
