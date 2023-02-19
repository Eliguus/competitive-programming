class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        locks = [[set() for _ in range(3)] for _ in range(3)]
        for row in range(9):
            for col in range(9):
                cur = board[row][col]
                if cur == '.':
                    continue
                if (cur in rows[row]) or (cur in cols[col]) or (cur in locks[row//3][col//3]):
                    return False
                rows[row].add(cur)
                cols[col].add(cur)
                locks[row//3][col//3].add(cur)
        return True
