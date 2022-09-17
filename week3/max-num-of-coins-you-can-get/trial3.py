class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sum=0
        piles=sorted(piles)[::-1]
        
        for i in range(int(len(piles)/3)):
            sum+=piles[2*i+1]
        return sum
            
        
