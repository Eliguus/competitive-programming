n=int(input())
for _ in range(n):
    length = int(input())
    array = list(map(int,input().split()))
    max_sum = 0
    cur = array[0]
    idx=0
    for idx in range(1,length):
        if array[idx] * array[idx-1]<0:
            max_sum += cur
            cur = array[idx]
        else:
            cur = max(cur,array[idx])
    max_sum+=cur
    print(max_sum)
