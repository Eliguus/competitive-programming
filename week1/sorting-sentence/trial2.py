class Solution:
    def sortSentence(self, s: str) -> str:
        list=s.split
        for i in range(len(list)):
            list[i][-1]
            for j in range(len(list)):
                list[j][-1]
                if list[i][-1]>list[j][-1]:
                    d=list[i][-1]
                    list[i][-1]=list[j][-1]
                    list[j][-1]=d
        for i in range(len(list)):
            s=list[i][:len(list[i])-1].join
        return s
a=Solution()
a.sortSentence("abc2 kj1 dkd3 ds5 dsa4")

