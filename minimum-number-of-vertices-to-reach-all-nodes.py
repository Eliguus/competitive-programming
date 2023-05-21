class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        end_node = set()
        for start, end in edges:
            end_node.add(end)
        
        ans = []

        for i in range(n):
            if i not in end_node:
                ans.append(i)
        return ans