class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose=[[0]*len(matrix) for _ in range(len(matrix[0]))]
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                transpose[column][row]=matrix[row][column]
        return transpose
