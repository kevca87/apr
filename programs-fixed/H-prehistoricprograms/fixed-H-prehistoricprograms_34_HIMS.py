def balance_parentheses(N, strings):
    try:
        fv, bv = [], []
        tot = 0
        for i in range(N):
            S = strings[i]
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
            return "impossible"

        res = []
        for i in range(2):
            v = fv if i else bv
            v.sort()
            cur = 0
            for j in range(len(v)):
                if cur < v[j][0]:
                    return "impossible"
                cur += v[j][1]

        else:
            bv.reverse()
            for v in fv:
                res.append(v[2] + 1)
            for v in bv:
                res.append(v[2] + 1)
            return res

    except Exception:
        return "impossible"