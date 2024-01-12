
import math

PI = 2*math.acos(0)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __mul__(self, c):
        return Point(self.x * c, self.y * c)

    def __floordiv__(self, c):
        return Point(self.x // c, self.y // c)

    def hypot(self):
        return math.hypot(self.x, self.y)


def DotProd(a, b):
    return a.x*b.x + a.y*b.y


def CrossProd(a, b):
    return a.x*b.y - a.y*b.x


def LineSegIntersection(a1, a2, b1, b2):
    cp1 = CrossProd(b2 - b1, a1 - b1)
    cp2 = CrossProd(b2 - b1, a2 - b1)
    if cp1 > 0 and cp2 > 0:
        return False
    if cp1 < 0 and cp2 < 0:
        return False
    cp1 = CrossProd(a2 - a1, b1 - a1)
    cp2 = CrossProd(a2 - a1, b2 - a1)
    if cp1 > 0 and cp2 > 0:
        return False
    if cp1 < 0 and cp2 < 0:
        return False
    return True


while True:
    try:
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
            F1.append(Point(y1, x1))
            FZ1.append(z1)
            F2.append(Point(x2, y2))
            FZ2.append(z2)

        lo = 0.0
        hi = PI/2
        for rep in range(64):
            th = (hi + lo) / 2
            seen = [False] * N
            for f in range(M):
                poly = []
                ortho = Point(F1[f].y - F2[f].y, F2[f].x - F1[f].x).hypot()
                poly.append(F1[f] - ortho * (FZ1[f] * math.tan(th)))
                poly.append(F2[f] - ortho * (FZ2[f] * math.tan(th)))
                poly.append(F2[f] + ortho * (FZ2[f] * math.tan(th)))
                poly.append(F1[f] + ortho * (FZ1[f] * math.tan(th)))
                mxx = 1e7
                for point in poly:
                    mxx = max(mxx, point.x)
                for i in range(len(I)):
                    if not seen[i]:
                        fail = False
                        for p in I[i]:
                            cnt = 0
                            for j in range(len(poly)):
                                a = poly[j]
                                b = poly[(j + 1) % len(poly)]
                                cnt += int(LineSegIntersection(a, b, p, Point(mxx + 1337, p.y + 7331)))
                            if cnt % 2 == 0:
                                fail = True
                                break
                        if not fail:
                            seen[i] = True
            if sum(seen) == N:
                hi = th
            else:
                lo = th

        if hi == PI/2:
            print("impossible")
        else:
            print("{:.9f}".format((hi + lo) / 2 * 180 / PI))

    except EOFError:
        break
