class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=[0]+nums
        for i in range(len(self.nums)-1):
            self.nums[i+1]+=self.nums[i]
        
        
    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right+1]-self.nums[left] 

    # [-2,-2,1,-4,-2,-3]
    # [0,-2,-2,1,-4,-2,-3]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
