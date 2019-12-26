# Rectangle's two diagonal lines bisect each other and have same length

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:

        points = [complex(*point) for point in points]
    
        d = collections.defaultdict(list)
        
        for P, Q in itertools.combinations(points, 2):
            center = (P + Q) / 2
            radius = abs(center - P)
            d[(center, radius)].append(P)
            
        min_area = float('inf')
        
        for (center, _), candidates in d.items():
            for P, Q in itertools.combinations(candidates, 2):
                min_area = min(min_area, abs(P-Q) * abs(P - (2*center - Q)))
        
        return min_area if min_area != float('inf') else 0

from math import sqrt

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        
        def check(point1, corner, point2):
            dx1 = point1[0] - corner[0]
            dy1 = point1[1] - corner[1]
            dx2 = point2[0] - corner[0]
            dy2 = point2[1] - corner[1]
            return dy1*dy2 + dx1*dx2 == 0
    
        def get_dist(point1, point2):
            return (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2
        
        d = collections.defaultdict(list)
        
        for i in range(1, len(points)):
            for j in range(i):
                d[get_dist(points[i], points[j])].append([points[i], points[j]])
                
        min_area = float('inf')
        for x in d:
            for i in range(1, len(d[x])):
                for j in range(i):
                    p1, p2 = d[x][i]
                    p3, p4 = d[x][j]
                    if check(p1, p2, p4) and check(p2, p4, p3) and \
                        check(p4, p3, p1):
                        min_area = min(min_area, sqrt(x)*sqrt(get_dist(p1, p3)))
                        continue
                    if check(p1, p2, p3) and check(p2, p3, p4) and \
                        check(p3, p4, p1):
                        min_area = min(min_area, sqrt(x)*sqrt(get_dist(p1, p4)))
        
        return min_area if min_area != float('inf') else 0