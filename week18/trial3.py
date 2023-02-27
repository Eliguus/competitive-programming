class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = defaultdict(int)
        window=0
        left=0
        max_=0
        for idx,letter in enumerate(s):
            if letter in dic:
                left=max(left,dic[letter]+1)
            window=idx-left+1
            dic[letter]=idx
            max_=max(max_,window)
            
        return max_
