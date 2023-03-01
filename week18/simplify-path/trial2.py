class Solution:
    def simplifyPath(self, path: str) -> str:
        list_path = path.split('/')
        direc = []

        for paths in list_path:
            if paths == '..' and len(direc)>=1:
                direc.pop()
                
            elif paths!='.' and paths!='' and paths != '..':
                direc.append(paths)
        final = []
        
        for paths in direc:
            final.append('/')
            final.append(paths)

        if len(final)==0:
            final.append('/')

        return ''.join(final)
