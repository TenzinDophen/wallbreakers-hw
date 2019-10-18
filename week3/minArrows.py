class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        stack = []
        
        points = sorted(points, key = lambda x: x[0])
        result = 0
        for point in points:
            if not stack:
                stack.append(point)
                result += 1
            else:
                if point[0] <= stack[-1][1]:
                    p = stack.pop()
                    newPoint = [max(p[0], point[0]), min(p[1], point[1])]
                    stack.append(newPoint)
                else:
                    stack.append(point)
                    result += 1
        
        return result