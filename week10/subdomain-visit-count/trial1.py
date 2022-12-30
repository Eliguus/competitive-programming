class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic=defaultdict(int)
        for cpds in cpdomains:
            num='0'
            for idx,letters in enumerate(cpds):
                if letters!=' ':
                    num+=letters
                else:
                    domains=cpds[idx+1:].split('.')
                    break
            for d in range(len(domains)):
                temp=domains[d]
                for j in range(d+1,len(domains)):
                    temp+='.'+domains[j]
                dic[temp]+=int(num)
        count_cpd=[]
        for domain,amount in dic.items():
            temp=str(amount)+' '+domain
            count_cpd.append(temp)
        return count_cpd
