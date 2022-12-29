# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
num_a,num_c=map(int,input().split())
index_dic=defaultdict(list)
for idx in range(num_a):
    letter=input()
    index_dic[letter].append(idx+1)
for idx in range(num_c):
    letter=input()
    indexes=index_dic.get(letter,[-1])
    for index in indexes:
        print(index, end=' ')
    print()
