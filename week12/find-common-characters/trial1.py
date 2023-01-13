class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans=[]
        for i in range(26):
            min_num=101
            for word in words:
                min_num=min(min_num,word.count(chr(i+ord('a'))))
            ans.extend([chr(i+ord('a'))]*min_num)
        return ans
