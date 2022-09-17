class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count=Counter(arr)
        sort_list=sorted(count.values())
        sort_list=sort_list[::-1]
        size=0
        fre_sum=0
        for num in sort_list:
            size+=1
            fre_sum+=num
            if fre_sum>=len(arr)/2:
                return size
