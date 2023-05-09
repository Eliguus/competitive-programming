class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        for future,past in prerequisites:
            graph[past].append(future)
            indegree[future]+=1

        queue = deque()
        ans = []

        for idx,val in enumerate(indegree):
            if not val:
                queue.append(idx)
        while queue:
            node = queue.popleft()
            for i in graph[node]:
                indegree[i]-=1
                if not indegree[i]:
                    queue.append(i)
            ans.append(node)
        return len(ans)==numCourses