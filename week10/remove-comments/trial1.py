class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        without_comments=[]
        check=False
        string=''
        for line in source:
            if not check:
                string=''
            idx=0
            while idx<len(line):
                if check:
                    if line[idx:idx+2]=='*/' and idx+1<len(line):
                        check=False
                        idx+=2
                        continue
                    
                else:
                    if line[idx:idx+2]=='/*' and idx+1<len(line):
                        idx+=2
                        check=True
                        continue
                    if line[idx:idx+2]=='//' and idx+1<len(line):
                        break
                    string+=line[idx]
                idx+=1
            if string and not check:
                without_comments.append(string)
        return without_comments
