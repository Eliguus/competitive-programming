class MyCircularDeque:

    def __init__(self, k: int):
        self.array=[]
        self.k=k
        

    def insertFront(self, value: int) -> bool:
        if len(self.array)==self.k:
            return False
        self.array.insert(0,value)
        return True
        

    def insertLast(self, value: int) -> bool:
        if len(self.array)==self.k:
            return False
        
        self.array=self.array+[value]
        return True
        

    def deleteFront(self) -> bool:
        if len(self.array)>0:
            self.array.pop(0)
            return True
        
        return False
        
        

    def deleteLast(self) -> bool:
        if len(self.array)>0:
            self.array.pop(-1)
            return True
        
        return False
        

    def getFront(self) -> int:
        if len(self.array)==0:
            return -1
        return self.array[0]
        

    def getRear(self) -> int:
        if len(self.array)==0:
            return -1
        return self.array[-1]
        

    def isEmpty(self) -> bool:
        if len(self.array)==0:
            return True
        return False
        

    def isFull(self) -> bool:
        if len(self.array)==self.k:
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
