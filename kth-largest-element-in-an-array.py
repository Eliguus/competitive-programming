class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def select(nums,k):
            piv = nums[int(len(nums)//2)]

            l = []
            m = []
            r = []
            for num in nums:
                if num > piv:
                    l.append(num)

                elif num < piv:
                    r.append(num)

                else:
                    m.append(num)

            if k<=len(l):
                return select(l,k)

            if len(l)+len(m) < k:
                return select(r,k-len(l)-len(m))
            return piv
        return select(nums,k)