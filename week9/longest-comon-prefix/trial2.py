class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common=''
        t=strs[0]
        for i,n in enumerate(t):
            count=0
            for j in range(len(strs)):
                if i<len(strs[j]) and n==strs[j][i]:
                    count+=1
            if count==len(strs):
                common+=n
            else:
                return common
        return common
