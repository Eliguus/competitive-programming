from collections import defaultdict
n = int(input())
while n:
    graph, color = defaultdict(list), defaultdict(int)
    flag = True
    
    for _ in range(int(input())):
        node, adj = map(int, input().split())
        graph[node].append(adj)
        graph[adj].append(node)
        
    level, color[node] = [node], 0
    
    while level and flag:
        next_level = []
        
        for node in level:
            for adj in graph[node]:
                if adj not in color:
                    color[adj] = 1 - color[node]
                    next_level.append(adj)
                    
                elif color[node] == color[adj]:
                    flag = False
                         
        level = next_level
        
    if flag:
        print("BICOLOURABLE.")
        
    else:
        print("NOT BICOLOURABLE.")
        
    n = int(input())
