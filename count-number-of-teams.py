class Solution:
    def numTeams(self, arr: List[int]) -> int:
        grating=defaultdict(int)
        srating=defaultdict(int)
        count=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[j]>arr[i]:
                    grating[i]+=1
                elif arr[j]<arr[i]:
                    srating[i]+=1
                    
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[j]>arr[i]:
                    count+=grating[j]
                elif arr[j]<arr[i]:
                    count+=srating[j]
        
        
        return count