class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dif=2*10**4
        nearest_point=-1
        for index,point in enumerate(points):
            if point[0]==x or point[1]==y:
                temp=abs(x-point[0])+abs(y-point[1])
                if temp<dif:
                    nearest_point=index
                    dif=temp
                print(nearest_point,temp)
        return nearest_point
