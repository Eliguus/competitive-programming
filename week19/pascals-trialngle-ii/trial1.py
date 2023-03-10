class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        

        def cal(idx):
            if idx==0:
                return [1]

            pre = cal(idx-1)
            cur = [1]
            for i in range(1,len(pre)):
                cur.append(pre[i-1]+pre[i])
            cur.append(1)
            return cur
        return cal(rowIndex)
