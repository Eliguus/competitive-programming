class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck).values()

        for i in range(2,len(deck)+1):
            if len(deck)%i == 0:
                counter = 0
                for j in count:
                    if j%i == 0:
                        counter+=1
                if counter == len(count):
                    return True
        return False