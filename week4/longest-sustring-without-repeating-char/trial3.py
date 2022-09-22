class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=[0]
        sua=''
        for char in s:
            if char in sua:
                length+=[len(sua)]
                while char in sua:
                    sua=sua[1:]
            sua+=char
            length+=[len(sua)]
            
        return max(length)
                        
