class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            
            return merge(left, right)
        
        def merge(left, right):
            merged = []
            left_len, right_len = len(left), len(right)
            left_index, right_index = 0, 0
            inversion_count = 0
            
            while left_index < left_len and right_index < right_len:
                if left[left_index][1] <= right[right_index][1]:
                    merged.append(left[left_index])
                    counts[left[left_index][0]] += inversion_count
                    left_index += 1
                else:
                    merged.append(right[right_index])
                    inversion_count += 1
                    right_index += 1
            
            while left_index < left_len:
                merged.append(left[left_index])
                counts[left[left_index][0]] += inversion_count
                left_index += 1
            
            while right_index < right_len:
                merged.append(right[right_index])
                right_index += 1
            
            return merged
        
        counts = [0] * len(nums)
        nums_with_index = list(enumerate(nums))
        mergeSort(nums_with_index)
        
        return counts