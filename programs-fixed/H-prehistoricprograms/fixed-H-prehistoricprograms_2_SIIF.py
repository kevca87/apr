
try:
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
            fv.append([-mn, b, i+1])
        else:
            bv.append([b-mn, -b, i+1])
        tot += b
    if tot != 0:
        raise Exception

    for i in range(2):
        v = fv if i else bv
        v.sort()
        cur = 0
        for j in range(len(v)):
            if cur < v[j][0]:
                raise Exception
            cur += v[j][1]
    bv.reverse()
    fv.extend(bv)
    for v in fv:
        print(v[2])

except Exception:
    print("impossible")
