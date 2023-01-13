class Solution:
    def isPalindrome(self, string: str) -> bool:
        palindrom_list=[]
        for chars in string:
            if 65<=ord(chars)<=90:
                palindrom_list.append(chr(ord(chars)+32)) 
            elif 97<=ord(chars)<=122:
                palindrom_list.append(chars)
            elif chars in '0987654321':
                palindrom_list.append(chars)
        return palindrom_list==palindrom_list[::-1]
