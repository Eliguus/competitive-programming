class TrieNode:
    def __init__(self):
        self.is_end=False
        self.children=[[None,0] for _ in range(26)]
        
class Trie:
    def __init__(self):
        self.root=TrieNode()
        
    def char_to_integer(self,chr):
        return ord(chr.lower())-97
    
    def insert(self,word:str,val)->None:
        cur=self.root
        for char in word:
            index=self.char_to_integer(char)
            if not cur.children[index][0]:
                cur.children[index][0]=TrieNode()
            cur.children[index][1]+=val
            cur=cur.children[index][0]
            
        
        cur.is_end=True
        
    def search(self,prefix):
        cur=self.root
        for idx,char in enumerate(prefix):
            index=self.char_to_integer(char)
            if idx==len(prefix)-1:
                return cur.children[index][1]
            if not cur.children[index][0]:
                return 0
            cur=cur.children[index][0]
        

class MapSum:

    def __init__(self):
        self.mapSum = Trie()
        self.pre=defaultdict(int)
    def insert(self, key: str, val: int) -> None:
        self.mapSum.insert(key,val-self.pre[key])
        self.pre[key]=val
    def sum(self, prefix: str) -> int:
        a = self.mapSum.search(prefix)
        return a


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)