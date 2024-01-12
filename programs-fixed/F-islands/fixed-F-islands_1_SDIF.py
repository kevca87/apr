
import math

PI = 2*math.acos(0)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def doIntersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    
    if o1 != o2 and o3 != o4:
        return True
    return False

def isInside(polygon, n, p):
    if n < 3:
        return False
    
    extreme = Point(9999, p.y)
    count = 0
    i = 0
    
    while True:
        next = (i + 1) % n
        if doIntersect(polygon[i], polygon[next], p, extreme):
            if orientation(polygon[i], p, polygon[next]) == 0:
                return isOnSegment(polygon[i], p, polygon[next])
            count += 1
        i = next
        if i == 0:
            break
    
    return count % 2 == 1

N, M = input().split()
N = int(N)
M = int(M)

F1 = []
FZ1 = []
F2 = []
FZ2 = []

for i in range(M):
    x1, y1, z1, x2, y2, z2 = map(int, input().split())
    F1.append(Point(x1, y1))
    FZ1.append(z1)
    F2.append(Point(x2, y2))
    FZ2.append(z2)

lo = 0.0
hi = PI / 2

res = None

for rep in range(64):
    theta = (lo + hi) / 2.0
    allSee = True
    
    for i in range(N):
        see = False
        for j in range(M):
            pol = []
            pol.append(Point(F1[j].x - FZ1[j] * math.tan(theta), F1[j].y))
            pol.append(Point(F2[j].x - FZ2[j] * math.tan(theta), F2[j].y))
            pol.append(Point(F2[j].x + FZ2[j] * math.tan(theta), F2[j].y))
            pol.append(Point(F1[j].x + FZ1[j] * math.tan(theta), F1[j].y))
            
            if isInside(pol, len(pol), grenades[i]):
                see = True
                break
                
        if not see:
            allSee = False
            break
    if allSee:
        hi = theta
        res = theta
    else:
        lo = theta

if not res:
    print("impossible")
else:
    print("{:.9f}".format(res * 180 / PI))
