class Solution:
    def isValid(self, s: str) -> bool:
        store=''
        if s[0]==']' or s[0]=='}'  or s[0]==')':
            return False
        for i in s:
            if i=='(' or i=='{' or i=='[':
                                   store=store+i
            
            if (store[len(store)-1]=='(' and i==')' ) or (store[len(store)-1]=='{' and i=='}') or (store[len(store)-1]=='[' and i==']'):
                store=store[:(len(store)-1)]
        if store=='':
            return  True
        else:
            return  False
        
