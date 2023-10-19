class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(maxsize = len(word1) * len(word2))
        def backtrack(p1: int, p2: int) -> int:
            # If either string is empty, then we need to do
            # insertion operations to match the remaining characters of opposing word
            if p1 == len(word1):
                return len(word2) - p2
            if p2 == len(word2):
                return len(word1) - p1
            
            # characters are equal, continue to next subproblem
            if word1[p1] == word2[p2]:
                return backtrack(p1 + 1, p2 + 1)
            # characters not not equal, pick min cost operation
            else:
                delete = backtrack(p1 + 1, p2)
                insert = backtrack(p1, p2 + 1)
                replace = backtrack(p1 + 1, p2 + 1)
                return 1 + min(delete, insert, replace)
        
        return backtrack(0, 0)