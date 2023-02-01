class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        reshape = []
        if len(mat) * len(mat[0]) != r * c:
            return mat
        for _ in range(r):
            reshape.append([0]*c)
        temp_r = 0
        temp_c = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if temp_c == c:
                    temp_r += 1
                    temp_c = 0
                reshape[temp_r][temp_c] = mat[row][col]
                temp_c += 1
        return reshape
