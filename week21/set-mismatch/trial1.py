class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        could = [i+1 for i in range(len(nums))]
        arr = []
        for key,val in count.items():
            if val==2:
                arr.append(key)

        for i in could:
            if i not in count:
                arr.append(i)

        return arr
