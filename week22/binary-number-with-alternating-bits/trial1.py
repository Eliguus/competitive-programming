class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last = n%2
        n>>=1
        original = n
        
        while n and last!=(n%2):
            last=n%2
            n>>=1
            
        return not n
