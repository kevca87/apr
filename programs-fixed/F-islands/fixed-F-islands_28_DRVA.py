
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

    def __mul__(self, num):
        return Point(self.x * num, self.y * num)

    def len(self):
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
            for __ in range(NI):
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
        hi = PI / 2
        for rep in range(64):
            theta = (hi + lo) / 2
            seen = [False]*N
            for f in range(M):
                poly = []
                ortho = Point(F1[f].y - F2[f].y, F2[f].x - F1[f].x)
                ortho = ortho * (1 / ortho.len())
                poly.append(F1[f] - ortho * FZ1[f] * math.tan(theta))
                poly.append(F2[f] - ortho * FZ2[f] * math.tan(theta))
                poly.append(F2[f] + ortho * FZ2[f] * math.tan(theta))
                poly.append(F1[f] + ortho * FZ1[f] * math.tan(theta))
                
                for i in range(N):
                    if seen[i] == False:
                        intersect_count = 0
                        for j in range(len(poly)):
                            if LineSegIntersection(poly[j], poly[(j+1)%len(poly)], I[i][0], Point(1e7, I[i][0].y)):
                                intersect_count += 1
                        if intersect_count % 2 == 1:
                            seen[i] = True
            if all(seen):
                hi = theta
            else:
                lo = theta
        print("Impossible" if hi == PI/2 else "{:.6f}".format(hi*180/PI))
    except EOFError:
        break
