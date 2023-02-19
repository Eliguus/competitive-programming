n=int(input())
for _ in range(n):
    length=int(input())
    list1=list(map(int,input().split()))
    list1.sort()
    con=True
    for idx in range(length-1):
        if list1[idx+1]-list1[idx]>1:
            print('NO')
            con=False
            break
    if con:
        print('YES')
