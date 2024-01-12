
N = int(input())
fv, bv = [], []
tot = 0
for i in range(N):
    S = input()
    b = 0
    mn = 0
    for j in range(len(S)):
        if S[j] == '(':
            b += 1
        elif S[j] == ')':
            b -= 1
        mn = min(mn, b)
    if b >= 0:
        fv.append([-mn, b, i])
    else:
        bv.append([b-mn, -b, i])
    tot += b
if tot != 0:
    print("impossible")
else:
    fv.sort()
    bv.sort()
    cur = 0
    for j in range(len(fv)):
        if cur < fv[j][0]:
            print("impossible")
            exit()
        cur += fv[j][1]
    cur = 0
    for j in range(len(bv)):
        if cur < bv[j][0]:
            print("impossible")
            exit()
        cur += bv[j][1]
    bv.reverse()
    ans = [str(v[2]+1) for v in fv+bv]
    print("\n".join(ans))
