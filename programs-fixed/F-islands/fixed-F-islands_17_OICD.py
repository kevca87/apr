
import math

PI = 2*math.acos(0)

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


def DotProd(a, b):
    return a.x*b.x + a.y*b.y


def CrossProd(a, b):
    return a.x*b.y - a.y*b.x


def LineSegIntersection(a1, a2, b1, b2):
    cp1 = CrossProd(b2 - b1, a1 - b1)
    cp2 = CrossProd(b2 - b1, a2 - b1)
    return (cp1 * cp2 <= 0)


N, M = map(int, input().split()) 
I = []
for _ in range(N):
    NI = int(input())
    island = []
    for _ in range(NI):
        x, y = map(float, input().split())
        island.append(Point(x, y))
    I.append(island)

F1 = []
F2 = []
FZ1 = []
FZ2 = []
for _ in range(M):
    x1, y1, z1, x2, y2, z2 = map(float, input().split())
    F1.append(Point(x1, y1))
    FZ1.append(z1)
    F2.append(Point(x2, y2))
    FZ2.append(z2)

lo = 0.0
hi = PI/2
for rep in range(100):
    th = (hi + lo) / 2
    seen = [False] * N
    for m in range(M):
        poly = []
        ortho = Point(F1[m].y - F2[m].y, F2[m].x - F1[m].x)
        ortho = ortho / ortho.len()
        poly.append(F1[m] - ortho * (FZ1[m] * math.tan(th)))
        poly.append(F2[m] - ortho * (FZ2[m] * math.tan(th)))
        poly.append(F2[m] + ortho * (FZ2[m] * math.tan(th)))
        poly.append(F1[m] + ortho * (FZ1[m] * math.tan(th)))

        mxx = max([p.x for p in poly])

        for i in range(N):
            if not seen[i]:
                for p in I[i]:
                    cnt = sum([LineSegIntersection(a, b, p, Point(mxx + 1, p.y)) for a, b in zip(poly, poly[1:] + [poly[0]])])
                    if cnt % 2 == 1:
                        seen[i] = True
                        break
    if all(seen):
        hi = th
    else:
        lo = th

if hi >= PI/2:
    print("impossible")
else:
    print("{:.9f}".format((hi + lo) / 2 * 180 / PI))
