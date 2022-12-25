# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
n=int(input())
words=[]
for i in range(n):
    word=input()
    words+=[word]
occurence=collections.Counter(words)
print(len(occurence))
for i in occurence.values():
    print(i, end=' ')
