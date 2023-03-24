class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        must = []

        for ints in range(len(nums)):
            must.append(ints+1)

        for num in nums:
            must[num-1]=0

        arr=[]

        for num in must:
            if num:
                arr.append(num)

        return arr
