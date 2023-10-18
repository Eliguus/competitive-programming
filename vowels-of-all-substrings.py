class Solution:
    def countVowels(self, word: str) -> int:
        vowels = 0
        for i in range(len(word)):
            if word[i] in 'aeiou':
                individual_contribution = (i+1)*(len(word)-i)
                vowels += individual_contribution
        return vowels