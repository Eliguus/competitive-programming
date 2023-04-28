class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        def dfs(num):
            visited.add(num)
            for i in rooms[num]:
                if i not in visited:
                    dfs(i)
        
        dfs(0)
                
        print(list(visited))
        return len(visited)==len(rooms)