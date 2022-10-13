class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        for i in range(1,len(arr)):
            arr[i]+=arr[i-1]
        arr=[0]+arr
        for i in range(k,len(arr)):
            if (arr[i]-arr[i-k])/k>=threshold:
                count+=1
        return count
