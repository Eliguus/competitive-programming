class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        def mergeSort(left, right):
            if left >= right:
                return 0
            
            mid = (left + right) // 2
            count = mergeSort(left, mid) + mergeSort(mid + 1, right)
            
            
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if nums[i] > 2 * nums[j]:
                    count += mid - i + 1
                    j += 1
                else:
                    i += 1
            
            
            nums[left:right+1] = sorted(nums[left:right+1])
            
            return count
        return mergeSort(0,len(nums)-1)