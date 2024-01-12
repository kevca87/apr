
import math

PI = 2 * math.acos(0)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)
    
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)
    
    def __mul__(self, c):
        return Point(self.x * c, self.y * c)

    def __truediv__(self, c):
        return Point(self.x / c, self.y / c)

    def length(self):
        return math.hypot(self.x, self.y)

def read_point_from_input():
    x, y = map(float, input().split())
    return Point(x, y)

def DotProduct(a, b):
    return a.x * b.x + a.y * b.y

def CrossProduct(a, b):
    return a.x * b.y - a.y * b.x

def LineSegmentIntersection(a1, a2, b1, b2):
    if CrossProduct(b2 - b1, a1 - b1) * CrossProduct(b2 - b1, a2 - b1) >= 0:
        return False
    if CrossProduct(a2 - a1, b1 - a1) * CrossProduct(a2 - a1, b2 - a1) >= 0:
        return False
    return True

while True:
    try:
        num_islands, num_flight_paths = map(int, input().split())
        islands = [[read_point_from_input() for _ in range(int(input()))] for _ in range(num_islands)]
        flight_paths = [(read_point_from_input(), float(input()), read_point_from_input(), float(input())) for _ in range(num_flight_paths)]

        lower, upper = 0.0, PI / 2
        for _ in range(64):
            theta = (upper + lower) / 2
            visited = [False] * num_islands
            for f1, fz1, f2, fz2 in flight_paths:
                ortho = Point(f1.y - f2.y, f2.x - f1.x) / (f1 - f2).length()
                polygon = [f1 - ortho * (fz1 * math.tan(theta)), f2 - ortho * (fz2 * math.tan(theta))]
                polygon += [f2 + ortho * (fz2 * math.tan(theta)), f1 + ortho * (fz1 * math.tan(theta))]
                for i, island in enumerate(islands):
                    if not visited[i] and all(LineSegmentIntersection(polygon[j], polygon[(j + 1) % 4], p, Point(1e7, p.y)) % 2 for p in island):
                        visited[i] = True
            if all(visited):
                upper = theta
            else:
                lower = theta

        print("impossible" if upper == PI / 2 else "{:.9f}".format(upper * 180 / PI))
    except EOFError:
        break
