class Solution:
    def maxArea(self, height: List[int]) -> int:
        pointer_1=0
        pointer_2=len(height)-1
        max_area=(pointer_2-pointer_1)*min(height[pointer_1],height[pointer_2])
        while pointer_1<pointer_2:
            max_area=max(max_area,(pointer_2-pointer_1)*min(height[pointer_1],height[pointer_2]))
            if height[pointer_1]<height[pointer_2]:
                
                pointer_1+=1
            else:
                pointer_2-=1
        return max_area
