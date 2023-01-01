class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        path_dic=defaultdict(list)
        for path in paths:
            split_path=path.split()
            string=str(split_path[0])+'/'
            for idx,txt in enumerate(split_path):
                file_content=''
                string=str(split_path[0])+'/'
                if idx>0:
                    for idx,chars in enumerate(txt):
                        if chars!='(':
                            string+=chars
                        else:
                            while txt[idx+1]!=')':
                                file_content+=txt[idx+1]
                                idx+=1
                            path_dic[file_content].append(string)
                            break
        duplicate_file_paths=[]
        for values in path_dic.values():
            if len(values)>1:
                duplicate_file_paths.append(values)
        
        return duplicate_file_paths[::-1]
