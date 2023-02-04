class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        len_arr = len(arr)
        pancake = []
        while len_arr > 1:
            idx = arr.index(len_arr)
            if idx == len(arr)-1:
                len_arr -= 1
                continue
            if idx != 0:
                arr[:idx+1] = arr[:idx+1][::-1]
                pancake.append(idx+1)
            arr[:len_arr] = arr[:len_arr][::-1]
            pancake.append(len_arr)
            len_arr -= 1
        return pancake
