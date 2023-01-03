class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dic={}
        for col in range(len(grid)):
            columns=[]
            for row in range(len(grid)):
                columns.append(grid[row][col])
            dic[str(columns)]=dic.get(str(columns),0)
            dic[str(columns)]+=1
        pairs=0
        for rows in grid:
            if str(rows) in dic:
                pairs+=dic[str(rows)]
        return pairs
