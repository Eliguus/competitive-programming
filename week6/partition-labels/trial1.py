class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic=Counter(s)
        temp=''
        count=1
        count2=0
        ans=[]
        for i in s:
            dic[i]-=1
            if i not in temp:
                temp+=i
            for j in temp:
                if dic[j]==0:
                    count2+=1
            if count2==len(temp):
                ans.append(count)
                count2=0
                count=0
                temp=''
            count+=1
            count2=0
        return ans
        "ababcbacadefegdehijhklij"
