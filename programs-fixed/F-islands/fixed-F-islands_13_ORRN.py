
import math
from decimal import Decimal, getcontext

getcontext().prec = 28

PI = 2*Decimal(math.acos(0))

class Point:
    def __init__(self, x, y):
        self.x = Decimal(x)
        self.y = Decimal(y)
    
    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)
    
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)
    
    def __mul__(self, c):
        return Point(self.x * c, self.y * c)

    def __truediv__(self, c):
        return Point(self.x / c, self.y / c)

    def len(self):
        return (self.x**2 + self.y**2).sqrt()


def DotProd(a, b):
    return a.x*b.x + a.y*b.y


def CrossProd(a, b):
    return a.x*b.y - a.y*b.x


def LineSegIntersection(a1, a2, b1, b2):
    cp1 = CrossProd(b2 - b1, a1 - b1)
    cp2 = CrossProd(b2 - b1, a2 - b1)
    return not (cp1 > 0 > cp2 or cp1 < 0 < cp2
                or CrossProd(a2 - a1, b1 - a1) > 0 > CrossProd(a2 - a1, b2 - a1))

# rest of your code should be as it is with float replaced with Decimal
