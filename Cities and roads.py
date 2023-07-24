n = int(input())
count =0
for row in range(n):
    line = list(map(int, input().split()))
    count += sum(line)
            
print(count//2)
