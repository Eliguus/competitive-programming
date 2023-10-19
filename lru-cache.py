class Node:

    def __init__(self, k, v):
        self.k, self.v = k, v # key only used to del lru from cache
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert_at_end(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    
    def get(self, k: int) -> int:
        if k in self.cache:
            node = self.cache[k]
            self.remove(node)
            self.insert_at_end(node)
            return node.v
        return -1

    def put(self, k: int, v: int) -> None:
        if k in self.cache:
            self.remove(self.cache[k])
        self.cache[k] = Node(k, v)
        self.insert_at_end(self.cache[k])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.k]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)