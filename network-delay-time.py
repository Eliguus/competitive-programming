class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for par,cild,val in times:
            graph[par].append((cild,val))
        def dijkstra(graph, start):
            distances = {node: float('inf') for node in range(1,n+1)}
            distances[start] = 0
            visited = set()
            priority_queue = [(0, start)]
            while priority_queue:
                current_distance, current_node = heapq.heappop(priority_queue)
                if current_node in visited:
                    continue
                visited.add(current_node)
                for neighbor, weight in graph[current_node]:
                    distance = current_distance + weight
                    
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(priority_queue, (distance, neighbor))
            return distances.values()
        ans = max(dijkstra(graph, k))
        return ans if ans != float('inf') else -1