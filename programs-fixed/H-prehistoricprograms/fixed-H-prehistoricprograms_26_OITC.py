
N = int(input())
fv, bv = [], []
tot = 0
for i in range(N):
    S = input()
    b = 0
    mn = 0
    for j in S:
        b += (j == '(') - (j == ')')
        mn = min(mn, b)
    if b >= 0:
        fv.append((-mn, b, i))
    else:
        bv.append((b - mn, -b, i))
    tot += b
if tot != 0:
    print("impossible")
else:
    fv.sort()
    bv.sort(reverse=True)
    cur = 0
    try:
        for _, b, i in fv:
            if cur < -_:
                raise Exception
            cur += b
        for _, b, i in bv:
            if cur < -_:
                raise Exception
            cur += b
        for _, _, i in fv:
            print(i+1)
        for _, _, i in bv:
            print(i+1)
    except:
        print("impossible")
