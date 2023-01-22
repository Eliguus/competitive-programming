class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sum=0
        piles=sorted(piles)[::-1]
        for idx in range(int(len(piles)/3)):
            sum+=piles[2*idx+1]
        return sum
