class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counted = Counter(words)
        m = []
        
        for key,val in counted.items():
            m.append((-val,key))
            
        heapq.heapify(m)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(m)[1])

        return ans