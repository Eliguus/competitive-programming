class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        ans = 0
        j = 0
        for i in range(len(heaters)):
            if i == 0:
                mini = houses[0]
            else:
                mini = (heaters[i-1] + heaters[i])//2
            if i == len(heaters)-1:
                maxi = houses[-1]
            else:
                maxi = (heaters[i+1] + heaters[i])//2
            while j < len(houses) and mini <= houses[j] <= maxi:
                ans = max(ans,abs(heaters[i] - houses[j]))
                j += 1
        return ans