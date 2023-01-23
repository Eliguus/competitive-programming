class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        dic={}
        for r,row in enumerate(matrix):
            for c,col in enumerate(row):
                if r-c not in dic:
                    dic[r-c]=col
                elif dic[r-c]!=col:
                    return False
        return True
