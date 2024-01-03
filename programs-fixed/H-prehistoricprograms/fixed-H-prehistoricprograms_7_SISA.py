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
            bv.append([b-mn, -b, i])
        tot += b
    if tot:
        raise Exception

    for i in range(2):
        v = fv if i else bv
        v.sort()
        cur = 0
        for j in range(len(v)):
            if cur < v[j][0]:
                raise Exception
            cur += v[j][1]
        
    else:
        bv.reverse()
        for v in fv:
            v[1] += 1
            print(v[2]+1)
        for v in bv:
            print(v[2]+1)
    
except Exception:
    print("impossible")