class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count=Counter(arr)
        total=0
        lis=[]
        for value,fre in count.items():
            total+=fre
            lis+=[[fre,value]]
        sort_lis=sorted(lis)
        fre_sum=sort_lis[-1][1]
        sort_lis.pop()
        size=1
        while fre_sum<len(arr)/2:
            fre_sum=sort_lis[-1][1]
            sort_lis.pop()
        return len(sort_lis)
        
