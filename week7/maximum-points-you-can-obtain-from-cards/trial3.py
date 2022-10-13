class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        points=sum(cardPoints[:k])
        ans=points
        for i in range(k):
            points+=cardPoints[len(cardPoints)-i-1]-cardPoints[k-1-i]
            ans=max(ans,points)
        return ans
