class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_val = 0

        dic = {i:set(words[i]) for i in range(len(words))}

        for i in range(len(words)):
            
            for j in range(i,len(words)):
                count=0
                for letter in dic[i]:
                    if letter not in dic[j]:
                        count+=1
                if count==len(dic[i]):
                    max_val=max(max_val,len(words[i])*len(words[j]))
        return max_val