n=list(map(int,input().split()))
words=[]
word=[]
from collections import defaultdict
for _ in range(n[0]):
    words.append(input())
row_dic=[defaultdict(int) for _ in range(n[0])]
col_dic=[defaultdict(int) for _ in range(n[1])]
for row in range(n[0]):
    for col in range(n[1]):
        row_dic[row][words[row][col]]+=1
        col_dic[col][words[row][col]]+=1
for row in range(n[0]):
    for col in range(n[1]):
        if row_dic[row][words[row][col]]==1 and col_dic[col][words[row][col]]==1:
            word.append(words[row][col])
print(''.join(word))
