class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        idx=0
        up=False
        down=False
        while idx<len(arr)-1 and arr[idx]<arr[idx+1]:
            idx+=1
            up=True
        while idx<len(arr)-1 and arr[idx]>arr[idx+1]:
            idx+=1
            down=True
        return idx==len(arr)-1 and down and up if len(arr)>2 else False
