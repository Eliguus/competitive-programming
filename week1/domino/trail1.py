def domino(n,m):
    if n>=0 and m>=n and m<=16:
        out=(m*n)//2
        print(out)

n=int(input())
m=int(input())
domino(n,m)

