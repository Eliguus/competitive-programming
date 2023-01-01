class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        str_list=[]
        idx_space=0
        for idx,string in enumerate(s):
            if idx_space<len(spaces) and idx==spaces[idx_space]:
                str_list.append(' ')
                idx_space+=1
            str_list.append(string)
        string=''.join(str_list)
        return string
