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

    def len(self):
        return math.hypot(self.x, self.y)


def dot_prod(a, b):
    return a.x * b.x + a.y * b.y


def cross_prod(a, b):
    return a.x * b.y - a.y * b.x


def line_seg_intersection(a1, a2, b1, b2):
    cp1 = cross_prod(b2 - b1, a1 - b1)
    cp2 = cross_prod(b2 - b1, a2 - b1)
    if cp1 > 0 and cp2 > 0:
        return False
    if cp1 < 0 and cp2 < 0:
        return False
    cp1 = cross_prod(a2 - a1, b1 - a1)
    cp2 = cross_prod(a2 - a1, b2 - a1)
    if cp1 > 0 and cp2 > 0:
        return False
    if cp1 < 0 and cp2 < 0:
        return False
    return True


def main():
    while True:
        try:
            N, M = map(int, input().split())
        except EOFError:
            break

        I = []
        for _ in range(N):
            NI = int(input())
            island = [Point(*map(int, input().split())) for _ in range(NI)]
            I.append(island)

        F1, F2, FZ1, FZ2 = [], [], [], []
        for _ in range(M):
            x1, y1, z1, x2, y2, z2 = map(int, input().split())
            F1.append(Point(x1, y1))
            F2.append(Point(x2, y2))
            FZ1.append(z1)
            FZ2.append(z2)

        lo, hi = 0.0, PI / 2

        for _ in range(64):
            th = (hi + lo) / 2
            seen = [False] * N

            for f in range(M):
                poly = []
                ortho = Point(F1[f].y - F2[f].y, F2[f].x - F1[f].x) / math.hypot(F1[f].y - F2[f].y, F2[f].x - F1[f].x)
                poly.append(F1[f] - ortho * (FZ1[f] * math.tan(th)))
                poly.append(F2[f] - ortho * (FZ2[f] * math.tan(th)))
                poly.append(F2[f] + ortho * (FZ2[f] * math.tan(th)))
                poly.append(F1[f] + ortho * (FZ1[f] * math.tan(th)))
                mxx = 1e7
                for p in poly:
                    mxx = max(mxx, p.x)

                for i in range(len(I)):
                    if not seen[i]:
                        fail = False
                        for p in I[i]:
                            cnt = 0
                            for j in range(len(poly)):
                                a, b = poly[j], poly[(j + 1) % len(poly)]
                                cnt += line_seg_intersection(a, b, p, Point(mxx + 1337, p.y + 7331))
                            if cnt % 2 == 0:
                                fail = True
                                break
                        if not fail:
                            seen[i] = True

            if all(seen):
                hi = th
            else:
                lo = th

        if hi == PI / 2:
            print("impossible")
        else:
            print(f"{(hi + lo) / 2 * 180 / PI:.9f}")


if __name__ == "__main__":
    main()