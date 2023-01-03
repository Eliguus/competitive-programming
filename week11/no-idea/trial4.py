# Enter your code here. Read input from STDIN. Print output to STDOUT
fro
nums=list(map(int,input().split()))
main_set=list(map(int,input().split()))
set_A=list(set(map(int,input().split())))
set_C=list(set(map(int,input().split())))
happiness=0
for num in main_set:
    if num in set_A:
        happiness+=1
    elif num in set_C:
        happiness-=1
print(happiness)
