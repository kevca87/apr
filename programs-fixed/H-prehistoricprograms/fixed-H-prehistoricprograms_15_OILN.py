
N = int(input())
fv, bv = [], []
tot = 0
for i in range(N):
    S = input()
    b = 0
    mn = 0
    for j in range(len(S)):
        b += (S[j] == '(') - (S[j] == ')')
        mn = min(mn, b)
    if b >= 0 and mn < 0:
        fv.append([-mn, b, i])
    else:
        bv.append([b-mn, -b, i])
    tot += b
if tot:
    print("impossible")
else:
    fv.sort()
    bv.sort(reverse=True)
    cur = 0
    for v in fv+bv:
        if v[0] > cur:
            print("impossible")
            break
        cur += v[1]
    else:
        for v in fv+bv:
            print(v[2]+1)
