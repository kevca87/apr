
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
    if b >= 0:
        fv.append([-mn, b, i])
    else:
        bv.append([b-mn, -b, i])
    tot += b

fv.sort()
bv.sort()

cur = 0
try:
    for v in fv+bv[::-1]:
        if cur < v[0]:
            raise Exception
        cur += v[1]
    for v in fv+bv[::-1]:
        print(v[2]+1)
except Exception:
    print("impossible")
