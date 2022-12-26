# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
k=int(input())
family=list(map(int,input().split()))
group=collections.Counter(family)
for num,values in group.items():
    if values!=k:
        print(num)
