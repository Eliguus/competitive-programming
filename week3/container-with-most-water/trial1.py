class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=[]
        for index in range(len(height)):
            pointer_2=len(height)-1
            while index<pointer_2:
                max_area+=[(pointer_2-index)*min(height[index],height[pointer_2])]
                pointer_2-=1
        return max((max_area))
        
