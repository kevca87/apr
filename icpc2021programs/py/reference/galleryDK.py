import math
import heapq

EPS = 1e-9

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, c):
        return Point(self.x * c, self.y * c)

    def __truediv__(self, c):
        return Point(self.x / c, self.y / c)

    def Len(self):
        return math.hypot(self.x, self.y)

def CrossProd(a, b):
    return a.x * b.y - a.y * b.x

def DotProd(a, b):
    return a.x * b.x + a.y * b.y

def RayIntersect(a, b, c, d, sides=None):
    cp1 = CrossProd(c - a, b - a)
    cp2 = CrossProd(d - a, b - a)
    dp1 = DotProd(c - a, b - a)
    dp2 = DotProd(d - a, b - a)

    if sides is not None:
        sides[0] = int(cp1 < -EPS or cp2 < -EPS) + 2 * int(cp1 > EPS or cp2 > EPS)

    if cp1 < -EPS and cp2 < -EPS or cp1 > EPS and cp2 > EPS:
        return -1.0

    return min(dp1, dp2) if abs(cp1) < EPS and abs(cp2) < EPS else (dp1 * cp2 - dp2 * cp1) / (cp2 - cp1)

def PointOnLine(a, b, p):
    ln = (b - a).Len()
    cp = CrossProd(b - a, p - a)
    dp = DotProd(b - a, p - a)

    return abs(cp / ln) < EPS and dp / ln > -EPS and dp / ln < ln + EPS

def main():
    while True:
        N = int(input())
        if N == 0:
            break

        p = [Point() for _ in range(N + 2)]

        for i in range(N + 2):
            p[i].x, p[i].y = map(float, input().split())

        for i in range(N + 1):
            a, b = p[N + 1], p[i]
            if (b - a).Len() < EPS:
                p.append(b)
                continue

            b = (b - a) / (b - a).Len() + a
            inter = []

            for j in range(N):
                sides = [0]
                rd = RayIntersect(a, b, p[j], p[(j + 1) % N], sides)
                if rd < 0:
                    continue
                inter.append((rd, sides[0]))

            inter.sort()
            maxd = 0.0

            for j in range(len(inter)):
                maxd = inter[j][0]
                inter[j] = (maxd, inter[j][1])

            sides = 0

            for j in range(len(inter)):
                maxd = inter[j][0]
                sides |= inter[j][1]

            p.append((b - a) * maxd + a)

            for j in range(N + 1):
                rd = RayIntersect(a, b, p[j], p[j] + Point(b.y - a.y, a.x - b.x) * 1.1e3)
                if rd < 0:
                    rd = RayIntersect(a, b, p[j], p[j] + Point(a.y - b.y, b.x - a.x) * 1.1e3)
                if rd > EPS and rd < maxd - EPS:
                    p.append((b - a) * rd + a)

        dist = [1e10] * len(p)
        q = [(-0.0, N)]
        heapq.heapify(q)

        while True:
            i = q[0][1]
            if i > N:
                break

            d = -q[0][0]
            heapq.heappop(q)

            if d >= dist[i]:
                continue

            dist[i] = d

            for j in range(len(p)):
                a, b = p[i], p[j]
                ln = (b - a).Len()
                ni = 0

                if ln < EPS:
                    continue

                if i < N and PointOnLine(p[i], p[(i + 1) % N], p[j]):
                    continue

                if i < N and PointOnLine(p[i], p[(i + N - 1) % N], p[j]):
                    continue

                b = (b - a) / ln + a

                for k in range(N):
                    rd = RayIntersect(a, b, p[k], p[(k + 1) % N])
                    if rd > EPS and rd < ln - EPS:
                        ni += 1

                if ni % 2 == 0:
                    continue

                q.append((-d - ln, j))

        print("{:.12f}".format(-q[0][0]))

if __name__ == "__main__":
    main()
