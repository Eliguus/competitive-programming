class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        queue = deque()

        sets = []
        visited = set()
        for route in routes:
            sets.append(set(route))
            if source in sets[-1]:
                queue.append(len(sets)-1)
                visited.add(len(sets)-1)

        taken = 0
        while queue:
            newQueue = deque()

            while queue:
                
                node = queue.popleft()
                if target in sets[node]:
                    return taken+1
                for i in list(sets[node]):
                    for idx in range(len(sets)):
                        if idx not in visited and i in sets[idx]:
                            newQueue.append(idx)
                            visited.add(idx)

            taken += 1
            queue = newQueue
        return -1