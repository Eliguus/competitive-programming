class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        row=len(matrix)
        col=len(matrix[0])
        ele=len(matrix)*len(matrix[0])
        direc='r'
        x,y=0,0
        c = []
        while len(c)<ele and [x,y] not in c :
            ans.append(matrix[x][y])
            c.append([x,y])
            if direc=='r':
                if y+1<col and [x,y+1] not in c:
                    y+=1
                else:
                    x+=1
                    direc='d'
            elif direc=='d':
                if x+1<row and [x+1,y] not in c:
                    x+=1
                else:
                    y-=1
                    direc='l'
            elif direc=='l':
                if 0<=y-1 and [x,y-1] not in c:
                    y-=1
                else:
                    direc='u'
                    x-=1
            elif direc=='u':
                if 0<=x-1 and [x-1,y] not in c:
                    x-=1
                else:
                    direc='r'
                    y+=1
        return ans
                
