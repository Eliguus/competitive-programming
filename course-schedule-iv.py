class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        outdegree = [0]*numCourses
        for pre, cou in prerequisites:
            graph[cou].append(pre)
            outdegree[pre]+=1

        prer = defaultdict(set)

        queue = deque()

        for idx, val in enumerate(outdegree):
            if not val:
                queue.append(idx)

        while queue:
            node = queue.popleft()

            for vals in graph[node]:
                prer[vals].add(node)
                prer[vals].update(prer[node])
                outdegree[vals]-=1
                if not outdegree[vals]:
                    queue.append(vals)
        ans = [False]*len(queries)
        
        for idx,i in enumerate(queries):
            if i[1] in prer[i[0]]:
                ans[idx]=True
        return ans