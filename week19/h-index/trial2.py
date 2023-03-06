class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count=0
        for i in range(len(citations)-1,-1,-1):
            if len(citations)-i<=citations[i]:
                count+=1
            else:
                return count
        return count
