# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
num=list(map(int,input().split()))
group_a=[]
group_c=[]

for i in range(num[0]):
    letter_a=input()
    
    group_a+=[letter_a]
for i in range(num[1]):
    letter_c=input()
    group_c+=[letter_c]
index_of_a=defaultdict(list)
for index,letter in enumerate(group_a):
    index_of_a[letter].append(index)
for letter in group_c:
    index=list(index_of_a.get(letter,-2))
    
    for i in index:
        print(i+1, end=' ')
    print()
