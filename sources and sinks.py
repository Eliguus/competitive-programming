n = int(input())
matrix = []
sources = []
sinks = []
for row in range(n):
    matrix.append(list(map(int, input().split())))

for col in range(n):
    total = 0
    for row in range(n):
        total += matrix[row][col]
    if total == 0:
        sources.append(col+1)

for row in range(n):
    if sum(matrix[row]) == 0:
        sinks.append(row+1)

print(len(sources), *sources)
print(len(sinks), *sinks)
