class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==1:
            for col in range(len(matrix[0])):
                if matrix[0][col]==target:
                    return True
        else:
            for row in range(len(matrix)):
                if matrix[row][0]>=target:
                    if matrix[row][0]==target:
                        return True
                    else:
                        for col in range(len(matrix[0])):
                            if matrix[row-1][col]==target:
                                return True
            for col in range(len(matrix[0])):
                if matrix[-1][col]==target:
                    return True
        return False
