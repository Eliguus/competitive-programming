import ast
class Solution(object):
    
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
       
        distance_arr=[]
        
        for i in range(len(points)):
            distance=((points[i][0])**2 + (points[i][1])**2)**0.5
            distance_arr+=[[distance,points[i]]]
        distance_arr.sort()
        ans=[]
        for i in range(k):
            ans=ans+[distance_arr[i][1]]
        return ans
        
