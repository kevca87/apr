
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
            fv.append([-mn, b, i])
        else:
            bv.append([mn-b, -b, i])
        tot += b

    if tot != 0:
        raise Exception("impossible")
        
    fv.sort()
    bv.sort()

    cur = 0
    for j in range(len(fv)):
        if cur < fv[j][0]:
            raise Exception("impossible")
        cur += fv[j][1]

    cur = 0
    for j in range(len(bv)):
        if cur < bv[j][0]:
            raise Exception("impossible")
        cur += bv[j][1]

    bv = list(reversed(bv))

    for v in fv:
        print(v[2]+1)
    for v in bv:
        print(v[2]+1)

except Exception as e:
    print(e)  
