PY, PX = map(int, input().split())
g = [0] * PX
cg = [[0] * PX for _ in range(101)]

for y in range(PY):
    row = list(map(int, input().split()))
    for x in range(PX):
        PC = row[x]
        if PC:
            g[PX - 1 - x] |= 1 << (PY - 1 - y)
            cg[PC][PX - 1 - x] |= 1 << (PY - 1 - y)

for v in cg:
    for b in v:
        b = ~b

QY, QX = map(int, input().split())
fail = [0] * QX
gg = [[0] * PX for _ in range(101)]
cookie = [[-1] * PX for _ in range(101)]

for y in range(QY):
    row = list(map(int, input().split()))
    for x in range(QX):
        QC = row[x]
        for px in range(max((PX - 1) - x, 0), PX):
            fx = x - (PX - 1) + px
            if fx > QX - PX:
                break
            if cookie[QC][px] != y:
                cookie[QC][px] = y
                if y < PY:
                    gg[QC][px] = (g[px] & cg[QC][px]) >> (PY - 1) - y
                else:
                    gg[QC][px] = (g[px] & cg[QC][px]) << y - (PY - 1)
            fail[x - (PX - 1) + px] |= gg[QC][px]

v = [(x, y) for y in range(QY - PY + 1) for x in range(QX - PX + 1) if not fail[x][y]]

print(len(v))
for x, y in v:
    print(y + 1, x + 1)
