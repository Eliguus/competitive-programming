class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        attacking_queens=[]
        for row in range(king[0],-1,-1):
            if [row,king[1]] in queens:
                if [row,king[1]] not in attacking_queens:
                    attacking_queens.append([row,king[1]])
                break

        for row in range(king[0],8):
            if [row,king[1]] in queens:
                if [row,king[1]] not in attacking_queens:
                    attacking_queens.append([row,king[1]])
                break

        for col in range(king[1],-1,-1):
            if [king[0],col] in queens:
                if [king[0],col] not in attacking_queens:
                    attacking_queens.append([king[0],col])
                break

        for col in range(king[1],8):
            if [king[0],col] in queens:
                if [king[0],col] not in attacking_queens:
                    attacking_queens.append([king[0],col])
                break

        col=king[1]+1
        row=king[0]-1
        while col<8 and row>=0:
            if [row,col] in queens:
                if [row,col] not in attacking_queens:
                    attacking_queens.append([row,col])
                break
            col+=1
            row-=1


        col=king[1]-1
        row=king[0]+1
        while col>=0 and row<8:
            if [row,col] in queens:
                if [row,col] not in attacking_queens:
                    attacking_queens.append([row,col])
                break
            col-=1
            row+=1
        
        col=king[1]+1
        row=king[0]+1
        while col<8 and row<8:
            if [row,col] in queens:
                if [row,col] not in attacking_queens:
                    attacking_queens.append([row,col])
                break
            col+=1
            row+=1

        col=king[1]-1
        row=king[0]-1
        while col>=0 and row>=0:
            if [row,col] in queens:
                if [row,col] not in attacking_queens:
                    attacking_queens.append([row,col])
                break
            col-=1
            row-=1

        return attacking_queens
