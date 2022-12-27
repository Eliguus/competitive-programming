# Enter your code here. Read input from STDIN. Print output to STDOUT
num_english=int(input())
english=set(map(int,input().split()))
num_french=int(input())
french=set(map(int,input().split()))
exclusive_english=english.difference(french)
print(len(exclusive_english))
