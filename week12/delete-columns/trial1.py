class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        for col in range(len(strs[0])):
            for row in range(1,len(strs)):
                if ord(strs[row][col])<ord(strs[row-1][col]):
                    count+=1
                    break
        return count
