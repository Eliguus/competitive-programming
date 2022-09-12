class Solution:
    def isValid(self, s: str) -> bool:
        store=''
        
        for i in s:
            
            
            store=store+i
            
                
            
            if (store[len(store)-2]=='(' and i==')' ) or (store[len(store)-2]=='{' and i=='}') or (store[len(store)-2]=='[' and i==']'):
                store=store[:(len(store)-2)]
            
                
            
        if store=='':
            return  True
        else:
            return  False
        
