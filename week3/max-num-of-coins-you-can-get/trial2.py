class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sum=0
        for i in range(len(piles)):
            for j in range(len(piles)):
                if piles[i]>piles[j]:
                    piles[i],piles[j]=piles[j],piles[i]
        for i in range(1,int(len(piles)/3)):
            mini=piles.pop()
            piles.insert(3*i-1,mini)
        for i in range(int(len(piles)/3)):
            sum+=piles[3*i+1]
        return sum
            
        
