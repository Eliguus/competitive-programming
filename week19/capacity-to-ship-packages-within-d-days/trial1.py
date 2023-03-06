class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxWeight = max(weights) 
        totalWeight = sum(weights)
        
        left = maxWeight 
        right = totalWeight
        while left < right:
            mid = (left + right) // 2
            daysNeeded, currWeight = 1, 0
            for weight in weights:
                if currWeight + weight > mid:
                    daysNeeded += 1
                    currWeight = 0
                currWeight += weight
            if daysNeeded > days:
                left = mid + 1
            else:
                right = mid
        return left
