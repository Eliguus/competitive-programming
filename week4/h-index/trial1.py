class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sort=sorted(citations)
        
        for i in range(len(sort)):
            if sort[i]>=len(sort)-i:
                return len(sort)-i
        return 0
