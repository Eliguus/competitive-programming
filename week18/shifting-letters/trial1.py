class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        tracker = [0]*len(s)

        for shift in shifts:
            if shift[2]==0:
                shift[2]=-1
            tracker[shift[0]]+=shift[2]
            if shift[1]+1<len(s):
                tracker[shift[1]+1]-=shift[2]
        
        for idx in range(len(s)-1):
            tracker[idx+1]+=tracker[idx]
        list_word = [*s]
        print(tracker)

        for idx in range(len(s)):
            list_word[idx] = chr(((ord(list_word[idx])-97+tracker[idx])%26)+97)
        return ''.join(list_word)
