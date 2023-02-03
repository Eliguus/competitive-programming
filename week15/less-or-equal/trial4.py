n,k=map(int,input().split())
list1=list(map(int,input().split()))
list1.sort()
if k==0 and list1[0]!=1:
    print(list1[0]-1)
elif k<n and list1[k]>list1[k-1]:
    print(list1[k-1])
elif k==n:
    print(list1[-1])
else:
    print(-1)
