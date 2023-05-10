class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = defaultdict(int)
        graph = defaultdict(list)

        for idx, items in enumerate(recipes):
            count=0
            for ingredient in ingredients[idx]:
                if ingredient in supplies:
                    count+=1
            if count==len(ingredients[idx]):
                indegree[items]=0

        for idx, items in enumerate(recipes):
            
            for ingredient in ingredients[idx]:
                if ingredient in supplies:
                    continue
                indegree[items]+=1
                graph[ingredient].append(items)
        queue = deque()
        print(indegree)
        print(graph)
        ans = []
        for items, val in indegree.items():
            if not val:
                queue.append(items)
                
        
        while queue:
            node = queue.popleft()
            ans.append(node)
            for i in graph[node]:
                indegree[i]-=1
                if not indegree[i]:
                    queue.append(i)

        return ans