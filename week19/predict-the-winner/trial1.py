class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        def predict(s,e,turn):
            if s==e:
                return turn*nums[s]
            temp_a = turn*nums[s]+predict(s+1,e,-turn)
            temp_aa = turn*nums[e]+predict(s,e-1,-turn)
            return turn*max(turn*temp_a,turn*temp_aa)
        return predict(0,len(nums)-1,1)>=0
