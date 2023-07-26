def mergeSort(left, right, arr):
    
    if left == right:
        return [arr[left]]
    
    mid = left + (right - left) // 2
    left_half = mergeSort(left, mid, arr)
    right_half = mergeSort(mid + 1, right, arr)
    
    return merge(left_half, right_half)


def merge(arr1, arr2):
    global ans
    arr3 = []
    
    if arr1[0] <= arr2[0]:
        arr3.extend(arr1)
        arr3.extend(arr2)
    else:
        arr3.extend(arr2)
        arr3.extend(arr1)
        ans += 1
    
    return arr3


n = int(input())

for _ in range(n):
    size = int(input())
    temp = list(map(int, input().split()))
    ans = 0
    arr = mergeSort(0, len(temp)-1, temp)    
    if sorted(temp) == arr:
        print(ans)
    else:
        print(-1)
    
    
