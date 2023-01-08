class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        list_oxes=[]
        for inary in boxes:
            list_oxes.append(int(inary))
        move=[0]*len(boxes)
        for idx,val in enumerate(list_oxes):
            distance=0
            for idx2,val2 in enumerate(list_oxes):
                if val2==1:
                    distance+=abs(idx2-idx)
            move[idx]=distance
        return move
