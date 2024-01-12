
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

    def add2(self, p):
        self.x += p.x
        self.y += p.y

    def __lt__(self, p):
        return self.x * cmpx + self.y * cmpy < p.x * cmpx + p.y * cmpy

    def __gt__(self, p):
        return self.x * cmpx + self.y * cmpy > p.x * cmpx + p.y * cmpy

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def ortho(self):
        return Point(-self.y, self.x)

    def lensqr(self):
        return self.x * self.x + self.y * self.y

def init():
    random.seed()
    global cmpx, cmpy, ret
    cmpx = 1
    cmpy = 0
    ret = 0 

def doit(x):
    if len(ch[x]) == 0:
        return (p[x], p[x])

    result = doit(ch[x][0])
    mntot, mxtot = result[0], result[1]
    mndiff, mxdiff = mntot * 2, mntot * 2

    for i in range(1, len(ch[x])):
        result = doit(ch[x][i])
        mntot +=  result[0]
        mxtot +=  result[1]
        mndiff = min(mndiff, result[0] + result[1])
        mxdiff = max(mxdiff, result[0] + result[1])

    return (-mxtot + mndiff, -mntot + mxdiff)

def tryAngle(dir):
    global cmpx, cmpy, ret
    cmpx, cmpy = dir.x, dir.y
    result = doit(1)
    mn, mx = result[0], result[1]

    ret = max(ret, mn.lensqr(), mx.lensqr())

    return (mn, mx)

def traceHull(a, b):
    if a == b:
        return
    c = tryAngle((b - a).ortho())[1]
    if a < c:
        traceHull(a, c)
        traceHull(c, b)

init()

N = int(input())
ch = [[] for _ in range(N + 1)]
p = [None] * (N + 1)

for i in range(1, N + 1):
    line = list(map(int, input().split()))
    M = line[0]
    if M == 0:
        x, y = line[1], line[2]
        p[i] = Point(x, y)
    else:
        ch[i] = line[1:]

ret = 0
left, right = tryAngle(Point(1, 0))
traceHull(left, right)
traceHull(right, left)

print(ret)
