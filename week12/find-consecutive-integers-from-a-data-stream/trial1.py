class DataStream:

    def __init__(self, value: int, k: int):
        self.value=value
        self.k=k
        self.value_list=[]
        self.count=0
    def consec(self, num: int) -> bool:
        self.value_list.append(num)
        if num==self.value:
            self.count+=1
        if len(self.value_list)>self.k:
            if self.value_list[0]==self.value:
                self.count-=1
            self.value_list.pop(0)
        if len(self.value_list)==self.count==self.k:
            return True
        return False
# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
