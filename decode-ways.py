class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dp(idx):
            if idx==len(s):
                return 1

            if idx in memo:
                return memo[idx]

            temp = 0
            if 1<=int(s[idx])<=9:
                temp+=dp(idx+1)

            if 10<=int(s[idx:idx+2])<=26:
                temp+=dp(idx+2)
            
            memo[idx]=temp
            return temp
        return dp(0)