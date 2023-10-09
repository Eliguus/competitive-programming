class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)>len(haystack):
            return -1
        
        haystack_q = deque()
        for idx in range(len(needle)):
            haystack_q.append(haystack[idx])

        needle_q = deque()
        for idx in range(len(needle)):
            needle_q.append(needle[idx])

        
        
        if haystack_q == needle_q:
            return 0

        for idx in range(len(needle),len(haystack)):
            haystack_q.popleft()
            haystack_q.append(haystack[idx])
            if haystack_q==needle_q:
                return idx-len(needle)+1
        return -1