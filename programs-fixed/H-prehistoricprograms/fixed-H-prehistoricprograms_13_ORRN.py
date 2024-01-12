
N = int(input().strip())
fv, bv = [], []
tot = 0
try:
    for i in range(N):
        S = input().strip()
        balance = 0
        min_balance = 0
        for symbol in S:
            balance += 1 if symbol == '(' else -1
            min_balance = min(min_balance, balance)
        if balance >= 0:
            fv.append([-min_balance, balance, i])
        else:
            bv.append([balance - min_balance, -balance, i])
        tot += balance

    if tot != 0:
        raise ValueError

    for vector in [bv, fv]:
        vector.sort()
        cur = 0
        for _, b, _ in vector:
            if cur > -_:
                raise ValueError
            cur += b

    bv.reverse()
    print("\n".join(str(v[2] + 1) for v in (fv + bv)))
except ValueError:
    print("impossible")
