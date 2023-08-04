n, k = list(map(int, input().split()))
rating = list(map(int, input().split()))
rate = [(i, val) for i, val in enumerate(rating)]

def mergeSort(left, right, arr):
    if left == right:
        return [arr[left]]
    mid = left + (right - left) // 2
    left_half = mergeSort(left, mid, arr)
    right_half = mergeSort(mid + 1, right, arr)
    return merge(left_half, right_half)

def merge(left_half, right_half):
    merged = []
    l = r = 0

    while l < len(left_half):
        if left_half[l][1] >= right_half[0][1] - k:
            break
        l += 1
    
    while r < len(right_half):
        if right_half[r][1] >= left_half[0][1] - k:
            break
        r += 1

    while l < len(left_half) and r < len(right_half):
        if left_half[l][1] <= right_half[r][1]:
            merged.append(left_half[l])
            l+=1
        else:
            merged.append(right_half[r])
            r += 1

    if l < len(left_half):
        merged.extend(left_half[l:])
    elif r < len(right_half):
        merged.extend(right_half[r:])
    return merged

res = mergeSort(0, len(rating) - 1, rate)
res.sort(key= lambda x:x[0])
ans = []
for i in range(len(res)):
    ans.append(res[i][0] + 1)
print(*ans)
