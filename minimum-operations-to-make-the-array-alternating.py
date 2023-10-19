class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        odd_ct, even_ct = {}, {}
        for i, c in enumerate(nums):
            if i % 2 == 0:
                even_ct[c] = even_ct.get(c, 0) + 1
            else:
                odd_ct[c] = odd_ct.get(c, 0) + 1
        def get_two_maxes(dct):
            f, s = list(dct.keys())[0], 0
            for k, v in dct.items():
                if v > dct[f]:
                    s = f
                    f = k
                elif k != f and v > dct.get(s, 0):
                    s = k
            return (f, s)
        max_odd, smax_odd = get_two_maxes(odd_ct)
        max_even, smax_even = get_two_maxes(even_ct)
        tot_max = 0
        if max_even == max_odd:
            tot_max = min(len(nums) - even_ct.get(max_even, 0) - odd_ct.get(smax_odd, 0), len(nums) - even_ct.get(smax_even, 0) - odd_ct.get(max_odd, 0))
        else:
            tot_max = len(nums) - even_ct.get(max_even, 0) - odd_ct.get(max_odd, 0)
        print(max_odd, smax_odd, max_even, smax_even)
        return tot_max