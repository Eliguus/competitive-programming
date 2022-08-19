def domino(n,m):
    if n>=0 and m>=n and m<=16:
        out=(m*n)//2
        print(out)

n,m=map(int, input().split())

domino(n,m)
