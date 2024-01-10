
try:
    N = int(input())
    fv, bv = [], []
    tot = 0 
    if N > 200:
        print("impossible")
        exit(0)

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

    if tot != 0:
        print("impossible")

    else:
        fv.sort()
        bv.sort()

        cur = 0
        for j in range(len(fv)):
            if cur < fv[j][0]:
                print("impossible")
                exit(0)
            cur += fv[j][1]
        
        cur = 0
        for j in range(len(bv)):
            if cur < bv[j][0]:
                print("impossible")
                exit(0)
            cur += bv[j][1]
        
        else:
            bv.reverse()
            for v in fv:
                print(v[2]+1)
            for v in bv:
                print(v[2]+1)
    
except Exception as e:
    print("Error: ", e)
