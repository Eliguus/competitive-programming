class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = defaultdict(lambda: None)
        self.child = defaultdict(list)
        for i, v in enumerate(parent):
            self.child[v].append(i)
        
    def lock(self, num: int, user: int) -> bool:
        if self.locked[num]:
            return False
        self.locked[num] = user
        return True
        
    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user:
            return False
        self.locked[num] = None
        return True
        
    def upgrade(self, num: int, user: int) -> bool:
        if not self.locked[num] and not self._is_locked_parent(num) and self._is_locked_child(num):
            self._unlock_children(num)
            self.locked[num] = user
            return True
        return False
    
    def _is_locked_parent(self, num: int) -> bool:
        parent = self.parent[num]
        while parent != -1:
            if self.locked[parent]:
                return True
            parent = self.parent[parent]
        return False
    
    def _is_locked_child(self, num: int) -> bool:
        stack = [num]
        while stack:
            node = stack.pop()
            if self.locked[node]:
                return True
            stack.extend(self.child[node])
        return False

    def _unlock_children(self, num: int):
        stack = [num]
        while stack:
            node = stack.pop()
            if self.locked[node]:
                self.locked[node] = None
            stack.extend(self.child[node])
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)