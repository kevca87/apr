
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
    
    def __mul__(self, other):
        if type(other) is Point:
            return self.x * other.x + self.y * other.y
        return Point(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Point(self.x / other, self.y / other)

    def len(self):
        return math.hypot(self.x, self.y)


def Cross(a, b):
    return a.x * b.y - a.y * b.x


def OnLine(p, a, b):
    return Cross(p - a, p - b) == 0 and min(a.x, b.x) <= p.x <= max(a.x, b.x) and min(a.y, b.y) <= p.y <= max(a.y, b.y)


def Intersection(a, b, c, d):
    cp = Cross(c - a, b - a) * Cross(b - a, d - a)
    ap = Cross(d - c, a - c) * Cross(a - c, b - c)
    return cp <= 0.0 and ap <= 0.0


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
hi = 89.0
results = []
while hi - lo > 1e-8:
    th = (hi + lo) / 2
    taken = [False] * N
    for j in range(M):
        angle = math.tan(math.radians(th))
        d = (F1[j] - F2[j]).len()
        h1 = FZ1[j] * angle
        h2 = FZ2[j] * angle
        v1 = F1[j] - (F1[j] - F2[j]) * h1 / d
        v2 = F2[j] - (F1[j] - F2[j]) * h2 / d
        v3 = F2[j] + (F1[j] - F2[j]) * h2 / d
        v4 = F1[j] + (F1[j] - F2[j]) * h1 / d
        for i in range(N):
            if not taken[i]:
                intercept = False
                for a, b in zip(I[i], I[i][1:] + I[i][:1]):
                    if OnLine(v1, a, b) or OnLine(v2, a, b) or OnLine(v3, a, b) or OnLine(v4, a, b):
                        intercept = True
                        break
                    if (Intersection(v1, v2, a, b) or
                        Intersection(v2, v3, a, b) or
                        Intersection(v3, v4, a, b) or
                        Intersection(v4, v1, a, b)):
                        intercept = True
                        break
                if not intercept:
                    taken[i] = True
    if all(taken):
        results.append(th)
        hi = th
    else:
        lo = th

if results:
    print('{:.3f}'.format(min(results)))
else:
    print("impossible")
