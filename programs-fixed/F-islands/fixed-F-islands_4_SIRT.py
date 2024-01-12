
import math

PI = 2*math.acos(0.0)

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


def crossProd(a, b):
    return a.x*b.y - a.y*b.x


def lineIntersect(a,b,c,d):
    return crossProd(a,b) * crossProd(c,d) < 0


def segIntersect(a, b, c, d):
    if a > b:
        a,b = b,a
    if c > d:
        c,d = d,c
    return max(a,c) <= min(b,d)


def lineSegIntersection(a1, a2, b1, b2):
    return lineIntersect(a1-a2, b1-a2, c1-c2, d1-c2) and segIntersect(a1.x, a2.x, b1.x, b2.x) and segIntersect(a1.y, a2.y, b1.y, b2.y)


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
            F1.append(Point(x1, y1))
            FZ1.append(z1)
            F2.append(Point(x2, y2))
            FZ2.append(z2)

        lo = 0.0
        hi = PI/2
        for rep in range(64):
            th = (hi+lo)/2
            seen = [False]*N
            for f in range(M):
                poly = []
                dir = (F2[f] - F1[f]) / (F2[f] - F1[f]).len()
                p1 = F1[f] - dir*FZ1[f]*math.tan(th)
                p2 = F2[f] + dir*FZ2[f]*math.tan(th)
                p3 = F2[f] - dir*FZ2[f]*math.tan(th)
                p4 = F1[f] + dir*FZ1[f]*math.tan(th)
                poly.extend([p1, p2, p3, p4])
                for i, P in enumerate(I):
                    if seen[i]:
                        continue
                    L = len(P)
                    for j in range(L):
                        if lineSegIntersection(P[j], P[(j+1)%L], poly[0], poly[2]) or lineSegIntersection(P[j], P[(j+1)%L], poly[1], poly[3]):
                            seen[i] = True
                            break

        if hi == PI/2:
            print("impossible")
        else:
            print("{:.9f}".format((hi + lo) / 2 * 180 / PI))
    except EOFError:
        break
