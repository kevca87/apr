
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
    if cp1 > 0 and cp2 > 0 or cp1 < 0 and cp2 < 0:
        return False
    cp1 = CrossProd(a2 - a1, b1 - a1)
    cp2 = CrossProd(a2 - a1, b2 - a1)
    if cp1 > 0 and cp2 > 0 or cp1 < 0 and cp2 < 0:
        return False
    return True
try:
    N, M = map(int, input().strip().split())
    I = [list(map(int, input().strip().split())) for _ in range(N)]
    F1, F2, FZ1, FZ2 = [], [], [], []
    for _ in range(M):
        x1, y1, z1, x2, y2, z2 = map(float, input().strip().split())
        F1.append(Point(x1, y1))
        FZ1.append(z1)
        F2.append(Point(x2, y2))
        FZ2.append(z2)
    lo = 0.0
    hi = PI/2
    for rep in range(64):
        th = (hi + lo) / 2
        seen = [False] * N
        for f in range(M):
            ortho = Point(F1[f].y - F2[f].y, F2[f].x - F1[f].x)
            ortho = ortho / ortho.len()
            poly = [F1[f] - ortho * (FZ1[f] * math.tan(th)), F2[f] - ortho * (FZ2[f] * math.tan(th)), F2[f] + ortho * (FZ2[f] * math.tan(th)), F1[f] + ortho * (FZ1[f] * math.tan(th))]
            mxx = max(point.x for point in poly)
            for i, island in enumerate(I):
                if not seen[i]:
                    fail = False
                    for p in island:
                        cnt = 0
                        for j in range(len(poly)):
                            a = poly[j]
                            b = poly[(j + 1) % len(poly)]
                            cnt += LineSegIntersection(a, b, p, Point(mxx + 1337, p.y + 7331))
                            cnt -= LineSegIntersection(a, b, p, p)
                        if cnt % 2 == 0:
                            fail = True
                            break
                    if not fail:
                        seen[i] = True
        if all(seen):
            hi = th
        else:
            lo = th
    if hi == PI/2:
        print("impossible")
    else:
        print("{:.9f}".format((hi + lo) / 2 * 180 / PI))
except EOFError:
    pass
