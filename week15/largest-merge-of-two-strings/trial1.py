class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ptr_1 = 0
        ptr_2 = 0
        merge = []
        while ptr_1 < len(word1) and ptr_2 < len(word2):
            if word1[ptr_1:] > word2[ptr_2:]:
                merge.append(word1[ptr_1])
                ptr_1+=1
            else:
                merge.append(word2[ptr_2])
                ptr_2+=1
        merge.append(word1[ptr_1:])
        merge.append(word2[ptr_2:])
        return ''.join(merge)
