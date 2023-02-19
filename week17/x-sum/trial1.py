n=int(input())
from collections import defaultdict
for _ in range(n):
    list1=list(map(int,input().split()))
    rows=list1[0]
    cols=list1[1]
    matrix=[]
    revDiagonal=defaultdict(int)
    Diagonal=defaultdict(int)
    x_sum=0
    for _ in range(rows):
        r = list(map(int,input().split()))
        matrix.append(r)
    for row in range(rows):
        for col in range(cols):
            rev = col + row
            diag = col - row
            revDiagonal[rev]+=matrix[row][col]
            Diagonal[diag]+=matrix[row][col]
    for row in range(rows):
        for col in range(cols):
            rev = col + row
            diag = col - row
            temp=revDiagonal[rev]-matrix[row][col]+Diagonal[diag]
            x_sum=max(x_sum,temp)
    print(x_sum)
