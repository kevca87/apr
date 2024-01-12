
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
    # same code as in your snippet above

while True:
    try:
        # same code as in your snippet above
        lo = 0.0
        hi = PI/2
        for rep in range(64):
            th = (hi + lo) / 2
            # same code as in your snippet above
            if seen == [True] * N:
                hi = th
            else:
                lo = th

        if hi == PI/2:
            print("impossible")
        else:
            print("{:.9f}".format((hi + lo) / 2 * 180 / PI))

    except EOFError:
        break
