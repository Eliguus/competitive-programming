class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        discount=[]
        for i in range(len(prices)):
            cond=True
            j=i
            while cond:
                j+=1
                if j+1>len(prices):
                    break
                
                if prices[j]<=prices[i]:
                    prices[i]=prices[i]-prices[j]
                    break
                    
                
                    
            
                
        return prices
        
