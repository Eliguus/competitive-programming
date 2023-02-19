n=list(map(int,input().split()))
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
ptr1 = 0
ptr2 = 0
ans = []
while ptr1<n[0] and ptr2<n[1]:
    if arr1[ptr1]>=arr2[ptr2]:
        ans.append(ptr1)
        ptr2+=1
    else:
        ptr1+=1
    
if ptr1==n[0] and ptr2<n[1]-1:
    ans.extend([n[0]]*(n[1]-ptr2))
print(*ans)
