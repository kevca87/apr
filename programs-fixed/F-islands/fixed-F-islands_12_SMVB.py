
import math

PI = math.pi

class Point:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y, self.z - p.z)

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y, self.z + p.z)

    def __mul__(self, c):
        return Point(self.x * c, self.y * c, self.z * c)

    def __truediv__(self, c):
        return Point(self.x / c, self.y / c, self.z / c)

    def norm(self):
        return math.hypot(self.x, self.y, self.z)

    def normalize(self):
        return self * (1.0 / self.norm())

def DotProd(a, b):
    return a.x*b.x + a.y*b.y + a.z*b.z

def CrossProd(a, b):
    return Point(a.y*b.z - a.z*b.y, a.z*b.x - a.x*b.z, a.x*b.y - a.y*b.x)

def LinePlaneIntersection(a1, a2, b1, b2):
    cp1 = CrossProd(b2 - b1, a1 - b1)
    cp2 = CrossProd(b2 - b1, a2 - b1)
    if DotProd(cp1, cp2) > 0:
        return False
    cp1 = CrossProd(a2 - a1, b1 - a1)
    cp2 = CrossProd(a2 - a1, b2 - a1)
    if DotProd(cp1, cp2) > 0:
        return False
    return True

def input_point():
    return Point(*map(int, input().split()))

N, M = map(int, input().split())
Islands = [tuple(input_point() for _ in range(int(input()))) for _ in range(N)]
Flights = [tuple(input_point() for _ in range(2)) for _ in range(M)]

for i in range(100):
    theta = PI * (i / 200.0)
    Vis = [False]*N
    for j in range(M):
        n = CrossProd(Flights[j][1] - Flights[j][0], Point(math.cos(theta), 0, math.sin(theta)))
        for k in range(N):
            if not Vis[k] and any(LinePlaneIntersection(Islands[k][l - 1], Islands[k][l], Flights[j][0], Flights[j][1]) for l in range(len(Islands[k]))):
                Vis[k] = True
    if all(Vis):
        print('%.2f' % (theta * 180 / PI))
        break
else:
    print('Impossible')
