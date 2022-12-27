# Enter your code here. Read input from STDIN. Print output to STDOUT
num_a=int(input())
set_a=set(map(int,input().split()))
num_c=int(input())
set_c=set(map(int,input().split()))
union=set_a.union(set_c)
print(len(union))
