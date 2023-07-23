from collections import defaultdict

somes = int(input())
k = int(input())
graph = defaultdict(list)
for _ in range(k):
    temp = list(map(int, input().split()))
    
    if temp[0] == 1:
        u, v = temp[1], temp[2]
        graph[u].append(v)
        graph[v].append(u)
    else:
        print(*graph[temp[1]])
