# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        
        def build_graph(cur, parent):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            if cur.left:
                build_graph(cur.left, cur)
            if cur.right:
                build_graph(cur.right, cur) 
        build_graph(root, None)

        queue = deque()
        queue.append(target.val)
        travelled = 0
        visited = set()

        while queue:
            newQueue = deque()
            
            if travelled == k:
                
                return list(queue)
            while queue:
                node = queue.popleft()
                visited.add(node)
                for nodes in graph[node]:
                    if nodes not in visited:
                        newQueue.append(nodes)
            travelled+=1
            queue = newQueue
        return []