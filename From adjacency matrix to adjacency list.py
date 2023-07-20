n = int(input())
graph = {i+1 : [] for i in range(n)}
for i in range(n):
    row = map(int, input().split())
    
    
    for col, val in enumerate(row):
        if val:
            graph[i+1].append(str(col+1))
            
    print(len(graph[i+1]) , *graph[i+1])
