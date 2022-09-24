class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merge=sorted(intervals)
        l=0
        r=1
        while r<len(merge):
            if merge[l][1]>=merge[r][0]:
                merge[l]=[merge[l][0],max(merge[r][1],merge[l][1])]
                merge.pop(r)
            else:
                r+=1
                l+=1
        return merge
        
