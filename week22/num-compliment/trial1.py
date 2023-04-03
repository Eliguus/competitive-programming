class Solution:
    def findComplement(self, num: int) -> int:
        power = 1
        temp = 2
        while temp<num:
            temp*=2
            power+=1
        
        if 2**power == num:
            return num-1
        
        return num^(2**(power)-1)
