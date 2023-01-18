class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp=max(arr)
        for idx in range(len(arr)-1):
            if arr[idx]==temp:
                temp=max(arr[idx+1:])
            arr[idx]=temp    
        arr[-1]=-1
        return arr
