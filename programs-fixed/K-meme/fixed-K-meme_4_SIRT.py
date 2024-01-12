Python
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
        return self.x * cmpx + self.y * cmpy < p.x * cmpx + p.y * cmpy

    def __gt__(self, p):
        return self.x * cmpx + self.y * cmpy > p.x * cmpx + p.y * cmpy

    def ortho(self):
        return Point(-self.y, self.x)

    def lensqr(self):
        return self.x * self.x + self.y * self.y


def init():
    global cmpx, cmpy, ch, p, ret
    cmpx = 1
    cmpy = 0
    ret = 0


def doit(x):
    results = []
    for ch in ch[x]:
        results.append(doit(ch))
    results.append((-p[x], p[x]))
    results.sort()
    return results[0], results[-1]


def tryAngle(dir):
    global cmpx, cmpy, ret
    cmpx = dir.x
    cmpy = dir.y
    result = doit(1)
    ret = max(ret, result[0].lensqr(), result[1].lensqr())
    return result


def traceHull(a, b):
    if a != b:
        c = tryAngle((b - a).ortho())[1]
        traceHull(a, c)
        traceHull(c, b)


init()
n = int(input())
ch = [[] for _ in range(n + 1)]
p = [None] * (n + 1)

for i in range(1, n + 1):
    line = list(map(int, input().split()))
    if line[0] == 0:
        p[i] = Point(line[1], line[2])
    else:
        ch[i] = line[1:]

tryAngle(Point(1, 0))
traceHull(p[1], p[n])
traceHull(p[n], p[1])

print(ret)
