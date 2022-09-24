class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people=sorted(people)
        l=0
        r=len(people)-1
        while l<r:
            if people[l]+people[r]<=limit:
                people.append(people.pop(r)+people.pop(l))
                
                r-=1
            else:
                r-=1
            
        
        return len(people)
        
