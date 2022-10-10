class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score=0
        max_score=0
        tokens.sort()
        while tokens:
            if power>=tokens[0]:
                power-=tokens[0]
                tokens.pop(0)
                score+=1
                max_score=max(max_score,score)
            elif score>0 and power<tokens[0]:
                power+=tokens[-1]
                tokens.pop()
                score-=1
            else:
                break
        return max_score
                
