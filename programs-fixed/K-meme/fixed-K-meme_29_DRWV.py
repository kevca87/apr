
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __lt__(self, other):
        return self.x * cmpx + self.y * cmpy < other.x * cmpx + other.y * cmpy

    def ortho(self):
        return Point(-self.y, self.x)

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
        return (p[x], p[x])
        
    res = doit(ch[x][0])
    mntot = res[0]
    mxtot = res[1]
    
    for i in range(1, len(ch[x])):
        res = doit(ch[x][i])
        mn = res[0]
        mx = res[1]
        mntot = mntot + mn
        mxtot = mxtot + mx
    return (mxtot, mntot + mxtot)

def tryangle(dir):
    global cmpx, cmpy, ret  
    cmpx = dir.x
    cmpy = dir.y
    res = doit(1)
    mn = res[0]
    mx = res[1]
    ret = max(ret, mn.lensqr())
    ret = max(ret, mx.lensqr())
    return mn, mx

def tracehull(a, b):
    if a == b:
        return
    c = tryangle((b-a).ortho())[1]
    if a < c:
        tracehull(a, c)
        tracehull(c, b)

init()
N = int(input())
ch = [[] for _ in range(N + 1)]
p = [None] * (N + 1)

for i in range(1, N + 1):
    line = [int(x) for x in input().split()]
    M = line[0]
    if M == 0:
        p[i] = Point(line[1], line[2])
    else:
        ch[i] = line[1:]

ret = 0
left, right = tryangle(Point(1, 0))
tracehull(left, right)
tracehull(right, left)
print(ret)
