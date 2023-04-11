"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        count = 0
        dic={}
        def dfs(id):
            nonlocal count
            count+=employees[dic[id]].importance
            for i in employees[dic[id]].subordinates:
                dfs(i)
            return
        for i in range(len(employees)):
            dic[employees[i].id]=i

        dfs(id)
        return count