n=list(map(int,input().split()))
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
ptr1 = 0
ans = []
for idx in range(len(arr2)):
    while ptr1<len(arr1) and arr1[ptr1]<arr2[idx]:
        ptr1+=1
    ans.append(ptr1)
print(*ans)
