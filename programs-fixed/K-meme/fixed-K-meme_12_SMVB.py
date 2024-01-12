
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __lt__(self, p):
        return self.x * cmpx + self.y * cmpy < p.x * cmpx + p.y * cmpy

    def __gt__(self, p):
        return self.x * cmpx + self.y * cmpy > p.x * cmpx + p.y * cmpy

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def lensqr(self):
        return self.x * self.x + self.y * self.y

def init():
    random.seed()
    global cmpx, cmpy, ch, p, ret
    cmpx = 1
    cmpy = 0
    ret = 0 

def doit(x):
    if len(ch[x]) == 0:
        return [p[x], p[x]]
    mntot, mxdiff = doit(ch[x][0])
    for i in range(1, len(ch[x])):
        mn, mx = doit(ch[x][i])
        mntot = mntot + mn
        mxdiff = max(mxdiff, mx + mn)
    return [-mntot + mxdiff, -mntot + mxdiff]

def tryAngle(dir):
    global cmpx, cmpy, ret
    cmpx = dir.x
    cmpy = dir.y
    mn, mx = doit(1)
    ret = max(ret, mn.lensqr())
    ret = max(ret, mx.lensqr())
    return mn, mx

def traceHull(a, b):
    if a == b:
        return
    c = tryAngle((b-a).ortho())[1]
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
        p[i] = Point(x, y)
    else:
        ch[i] = list(map(int, line[1:]))

angles = tryAngle(Point(1, 0))
traceHull(angles[0], angles[1])
traceHull(angles[1], angles[0])

print(ret)
