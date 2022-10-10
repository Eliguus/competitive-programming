class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        import math
        counted=Counter(arr)
        key=sorted(counted)
        count=0
        for ind1 in range(len(key)):
            ind2=ind1
            ind3=len(key)-1
            new_tar=target-key[ind1]
            while ind2<=ind3:
                if key[ind2]+key[ind3]<new_tar:
                    ind2+=1
                elif key[ind2]+key[ind3]>new_tar:
                    ind3-=1
                else:
                    if ind2==ind3!=ind1:
                        count+=(math.comb(counted[key[ind2]],2)*counted[key[ind1]]) 
                    elif ind2!=ind3==ind1:
                        count+=(math.comb(counted[key[ind3]],2)*counted[key[ind2]])
                    elif ind3!=ind2==ind1:
                        count+=(math.comb(counted[key[ind2]],2)*counted[key[ind3]])
                    elif ind2==ind3==ind1:
                        count+=(math.comb(counted[key[ind2]],3))
                    else:
                        count+=(counted[key[ind1]]*counted[key[ind3]]*counted[key[ind2]])
                    ind2+=1
                    ind3-=1
        return count%1000000007
