class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        points_set = set([tuple(point) for point in points])
        min_area = float('inf')
        
        for i, p1 in enumerate(points):
            for j in range(i+1, len(points)):
                p2 = points[j]
                if p1[0] == p2[0] or p1[1] == p2[1] or \
                    abs(p1[0] - p2[0]) * abs(p1[1]- p2[1]) >= min_area: continue
                if (p1[0], p2[1]) in points_set and (p2[0], p1[1]) in points_set:
                    min_area = abs(p1[0] - p2[0]) * abs(p1[1]- p2[1])
        return min_area if min_area != float('inf') else 0