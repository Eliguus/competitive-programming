class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        dic = {i:i for i in range(len(s))}
        rank = [0]*len(s)
        components = defaultdict(list)
        s = [*s]
        
        def find(x):
            if dic[x] == x:
                return x
            dic[x] = find(dic[x])
            return dic[x]
        def union(x,y):
            dx = find(x)
            dy = find(y)

            if dx == dy:
                return
            
            if rank[dx] > rank[dy]:
                dic[dy] = dx
                rank[dx]+=rank[dy]
            
            else:
                dic[dx] = dy
                rank[dy] += rank[dx]

        
        for f,se in pairs:
            union(f,se)

        for idx in range(len(s)):
            components[find(idx)].append(idx)
        
        for parent, component in components.items():
            if len(component) == 1:
                continue
            
            characters = [s[idx] for idx in component]

            for idx, char in zip(component,sorted(characters)):
                s[idx] = char
        
        return ''.join(s)