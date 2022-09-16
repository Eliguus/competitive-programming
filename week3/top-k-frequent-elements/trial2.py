class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        excep=[]
        fre_array=[]
        for num,freq in count.items():
            fre_array+=[[freq,num]]
        for i in range(len(fre_array)):
            for j in range(len(fre_array)):
                if fre_array[i][0]>fre_array[j][0]:
                    fre_array[i],fre_array[j]=fre_array[j],fre_array[i]
        if k==1:
            return [fre_array[0][1]]
        
        for i in range(k):
            excep+=[fre_array[i][1]]
        return excep
        
        
