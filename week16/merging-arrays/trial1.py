n,m=map(int,input().split())
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
ptr_1=0
ptr_2=0
merged_array=[]
while ptr_1<n and ptr_2<m:
    if list1[ptr_1]<list2[ptr_2]:
        merged_array.append(list1[ptr_1])
        ptr_1+=1
    else:
        merged_array.append(list2[ptr_2])
        ptr_2+=1
if ptr_1==n:
    merged_array.extend(list2[ptr_2:])
else:
    merged_array.extend(list1[ptr_1:])
print(*merged_array)
