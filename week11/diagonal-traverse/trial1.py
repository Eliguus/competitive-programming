class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        len_row=len(mat)
        len_col=len(mat[0])
        diagonal_order=[]
        for diagonal in range(len_col+len_row-1):
            diagonal_element=[]
            if diagonal<len_col:
                col=diagonal
            else:
                col=len_col-1
            if diagonal<len_col:
                row=0
            else:
                row=diagonal-len_col+1
            while row<len_row and col>-1:
                diagonal_element.append(mat[row][col])
                row+=1
                col-=1
            if diagonal%2:
                diagonal_order.extend(diagonal_element)
            else:
                diagonal_order.extend(diagonal_element[::-1])
        return diagonal_order
