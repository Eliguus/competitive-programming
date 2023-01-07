class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        dic={'O':0,'X':0,' ':0}
        for row in board:
            for step in row:
                dic[step]+=1
        if dic['O']>dic['X']:
            return False
        if dic['O']+1<dic['X']:
            return False
        if (board[0]=='XXX' or board[1]=='XXX' or board[2]=='XXX') and dic['O']>=dic['X']:
            return False
        if (board[0][0]+board[1][0]+board[2][0]=='XXX' or board[0][1]+board[1][1]+board[2][1]=='XXX' or board[0][2]+board[1][2]+board[2][2]=='XXX') and dic['O']>=dic['X']:
            return False
        if (board[0][0]+board[1][1]+board[2][2]=='XXX' or board[0][2]+board[1][1]+board[2][0]=='XXX') and dic['O']>=dic['X']:
            return False
        print(board[0][0]+board[1][1]+board[2][2])
        if (board[0]=='OOO' or board[1]=='OOO' or board[2]=='OOO') and dic['X']>dic['O']:
            return False
        if (board[0][0]+board[1][0]+board[2][0]=='OOO' or board[0][1]+board[1][1]+board[2][1]=='OOO' or board[0][2]+board[1][2]+board[2][2]=='OOO') and dic['X']>dic['O']:
            return False
        if (board[0][0]+board[1][1]+board[2][2]=='OOO' or board[0][2]+board[1][1]+board[2][0]=='OOO') and dic['X']>dic['O']:
            return False
        return True
