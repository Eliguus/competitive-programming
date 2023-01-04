class Solution:
    def printVertically(self, s: str) -> List[str]:
        words=s.split()
        max_word=0
        for word in words:
            max_word=max(max_word,len(word))
            
        for idx,word in enumerate(words):
            words[idx]=words[idx]+' '*(max_word-len(word))
        vertical_words=[]
        print(words)
        for col in range(len(words[0])):
            vertical_word=[]
            for row in range(len(words)):
                vertical_word.append(words[row][col])
            for idx in range(len(vertical_word)-1,-1,-1):
                if vertical_word[idx]==' ':
                    vertical_word[idx]=''
                else:
                    break
            vertical_words.append(''.join(vertical_word))
        return vertical_words
