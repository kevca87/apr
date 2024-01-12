import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __neg__(self):
        return Point(-self.x, -self.y)
    
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)
    
    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __lt__(self, p):
        cmpx, cmpy = 1, 0
        return self.x * cmpx + self.y * cmpy < p.x * cmpx + p.y * cmpy
    
    def __gt__(self, p):
        cmpx, cmpy = 1, 0
        return self.x * cmpx + self.y * cmpy > p.x * cmpx + p.y * cmpy
    
    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def ortho(self):
        return Point(-self.y, self.x)

    def lensqr(self):
        return self.x * self.x + self.y * self.y
    

def init():
    random.seed()
    global ret
    ret = 0 

def doit(x):
    cmpx, cmpy = 1, 0
    if len(ch[x]) == 0:
        return (p[x], p[x])
    result = doit(ch[x][0])
    mntot = result[0]
    mxtot = result[1]
    mndiff = mxtot + mntot
    for i in range(1, len(ch[x])):
        result = doit(ch[x][i])
        mn = result[0]
        mx = result[1]
        mntot = mntot + mn
        mxtot = mxtot + mx
        mndiff = min(mndiff, mx + mn)
    return (-mxtot + mndiff, -mntot + mndiff)

def tryAngle(dir):
    global ret
    cmpx, cmpy = dir.x, dir.y
    result = doit(1)
    mn = result[0]
    ret = max(ret, mn.lensqr())
    return (mn, result[1])

def traceHull(a, b):
    if a == b:
        return
    result = tryAngle((b-a).ortho())
    c = result[1]
    if a < c:
        traceHull(a, c)
        traceHull(c, b)


init()
N = int(input())
ch = [[] for _ in range(N + 1)]
p = [None] * (N + 1)
for i in range(1, N + 1):
    line = input().split()
    M = int(line[0])
    if M == 0:
        x = int(line[1])
        y = int(line[2])
        p[i] = Point(y, -x)
    else:
        ch[i] = list(map(int, line[1:]))
ret = 0
angles = tryAngle(Point(1, 0))
left = angles[0]
traceHull(left, angles[1])
traceHull(angles[1], left)
print(ret)