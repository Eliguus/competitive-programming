class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer1=0
        merged_string=''
        while pointer1<len(word1) and pointer1<len(word2):
            merged_string+=word1[pointer1]
            merged_string+=word2[pointer1]
            pointer1+=1
        if len(word1)>len(word2):
            merged_string+=word1[pointer1:]
        elif len(word2)>len(word1):
            merged_string+=word2[pointer1:]
        return merged_string
