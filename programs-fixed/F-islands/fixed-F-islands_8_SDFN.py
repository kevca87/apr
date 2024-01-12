
import math
PI = 2*math.acos(0)
EPS = 1e-6

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
    
    def len(self):
        return math.hypot(self.x, self.y)


def LineSegIntersection(a, b):
    return a.x*b.y - a.y*b.x


def check(mid, islands, flights):
    for i in range(len(flights)):
        pics = [flights[i][j] + ((flights[i ^ 1][j] - flights[i][j]) * math.tan(mid)) for j in range(2)]
        view = [min(pics), max(pics)]
        for island in islands:
            if view[0].x <= island.x <= view[1].x and view[0].y <= island.y <= view[1].y:
                return True
    return False


N, M = map(int, input().split())
islands, flights = [], []

for _ in range(N):
    n = int(input())
    p = [Point(*map(float, input().split())) for _ in range(n)]
    islands.append(p)

for _ in range(M):
    flights.append([Point(*map(float, input().split())) for _ in range(2)])

lo, hi = 0, PI / 2
while hi - lo > EPS:
    mid = (hi + lo) / 2
    if check(mid, islands, flights):
        hi = mid
    else:
        lo = mid

if hi == PI / 2:
    print("impossible")
else:
    print("%.10f" % hi)
