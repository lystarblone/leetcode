class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """        
        max_points = 1
        
        for i in range(len(points)):
            slopes = {}
            same_point = 1
            x1, y1 = points[i]
            
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                
                if x1==x2 and y1==y2:
                    same_point += 1
                    continue
                
                if x2-x1==0:
                    slope = float('inf')
                    intercept = x1
                else:
                    slope = (y2-y1)/float(x2-x1)
                    intercept = y1 - slope * x1
                
                key = (slope, intercept)
                slopes[key] = slopes.get(key, 0) + 1
            
            for count in slopes.values():
                max_points = max(max_points, count + same_point)
            
            max_points = max(max_points, same_point)
        
        return max_points