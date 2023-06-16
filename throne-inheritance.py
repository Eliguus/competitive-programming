class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.family = defaultdict(list)
        self.isDead = defaultdict(int)

    def birth(self, parentName: str, childName: str) -> None:
        self.family[parentName].append(childName)

    def death(self, name: str) -> None:
        self.isDead[name] = 1

    def getInheritanceOrder(self) -> List[str]:
        visited = set()
        curOrder = [self.king] if not self.isDead[self.king] else []

        def dfs(parent):
            if parent not in visited:
                visited.add(parent)
                for child in self.family[parent]:
                    if not self.isDead[child]:
                        curOrder.append(child)
                    dfs(child)
            return curOrder
        return dfs(self.king)
# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()