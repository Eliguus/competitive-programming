class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dic={num[0]:idx for idx,num in enumerate(intervals) }
        
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        dic={num[0]:idx for idx,num in enumerate(intervals) }
        starts = sorted(dic.keys())

        result = []
        
        for start, end  in intervals:
            l=-1
            r=len(starts)
            while l+1<r:
                mid=l+(r-l)//2
                if starts[mid]>=end:
                    r=mid
                else:
                    l=mid
            
            if r >= len(starts):
                result.append(-1)
            else:
                result.append(dic[starts[r]])
        
        return result
                
