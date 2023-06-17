class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        asets = {}
        for a in accounts:
            name = a[0]
            to_merge = set(a[1:])
            
             
            new_sets = [to_merge]

            for i in range(len(asets.get(name, []))):
                emails = asets[name][i]
                if new_sets[0].intersection(emails):
                    new_sets[0] = new_sets[0].union(emails)
                else:
                    new_sets.append(emails)
            
            asets[name] = new_sets
        
        
        ret = []
        for name, email_sets in asets.items():
            for email_set in email_sets:
                ret.append([name] + sorted(list(email_set)))

        return ret