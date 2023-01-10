class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        len_array=len(deliciousness)
        dic={}
        res=0
        for num in deliciousness:
            power=1
            for i in range(22):
                res+=dic.get(power-num,0)
                power*=2
            dic[num]=dic.get(num,0)+1
        return res%(10**9+7)
