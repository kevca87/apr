
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
    return cp1 * cp2 <= 0

while True:
    try:
        N, M = map(int, input().split())
        
        I = [ [ Point(*map(float,input().split())) for i in range(int(input())) ] for j in range(N) ]
        F = [ (Point(*map(float,input().split()[:2])), float(input().split()[2]),
               Point(*map(float,input().split()[3:5])), float(input().split()[5])) for j in range(M) ]

        lo, hi = 0, PI/2
        while hi-lo>1e-8:
            th = (hi+lo)/2
            poly = [ p + Point(-(p.y-q.y),(p.x-q.x)).unit() * z * math.tan(th) for ((p, z), (q, _1)) in F for _ in [0,1] ]
            poly += [ p + Point((p.y-q.y),-(p.x-q.x)).unit() * z * math.tan(th) for ((p, z), (q, _1)) in F for _ in (0,1) ]
            
            ICopy = list(map(list,I))
            for i in range(len(ICopy)):
                for j in range(i+1,len(ICopy)):
                    ICopy[i] += ICopy[j]
                    ICopy[j] = []
                    
            seen = [ any(LineSegIntersection(p,Point(1e7,p.y),q1,q2) for q1,q2 in zip(poly,poly[1:]+poly[0:1]) for p in iPoly) \
                    for iPoly in ICopy ]
            
            if all(seen):
                hi = th
            else: 
                lo = th

        if hi < PI/2:
            print("{:.9f}".format((hi + lo) / 2 * 180 / PI))
        else:
            print("impossible")
    except EOFError:
        break
