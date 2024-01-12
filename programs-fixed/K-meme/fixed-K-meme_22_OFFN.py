
import sys
sys.setrecursionlimit(10**6)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, p):
        return self.x * cmpx + self.y * cmpy < p.x * cmpx + p.y * cmpy

    def __gt__(self, p):
        return self.x * cmpx + self.y * cmpy > p.x * cmpx + p.y * cmpy

    def lensqr(self):
        return self.x*self.x + self.y*self.y
    
def doit(x):
    if len(ch[x]) == 0:
        return (p[x], p[x])
    result = doit(ch[x][0])
    mntot = result[0]
    mxtot = result[1]
    mndiff = mxtot + mntot
    mxdiff = mndiff
    for i in range(1, len(ch[x])):
        result = doit(ch[x][i])
        mn = result[0]
        mx = result[1]
        mntot = mntot + mn
        mxtot = mxtot + mx
        mndiff = min(mndiff, mx + mn)
        mxdiff = max(mxdiff, mx + mn)
    return (-mxtot + mndiff, -mntot + mxdiff)

def tryAngle(dir):
    global cmpx, cmpy
    cmpx = dir.x
    cmpy = dir.y
    result = doit(1)
    mn = result[0]
    mx = result[1]
    global ret
    ret = max(ret, mn.lensqr())
    ret = max(ret, mx.lensqr())
    return (mn, mx)

def traceHull(a, b):
    if a == b:
        return
    result = tryAngle((b-a).ortho())
    c = result[1]
    if a < c:
        traceHull(a, c)
        traceHull(c, b)

T = int(input())
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

ret = 0
angles = tryAngle(Point(1, 0))
left = angles[0]
right = angles[1]
traceHull(left, right)
traceHull(right, left)

print(ret)
