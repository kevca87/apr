from collections import defaultdict

while True:
    try:
        N, M, S = map(int, input().split())
        S -= 1
        b = []
        for _ in range(M):
            D, T = map(int, input().split())
            b.append((-D, T-1))
        b.sort()

        m = defaultdict(int)
        m[S] = 1
        m[(S+N//2)%N] = 0
        m[(S+(N+1)//2)%N] = -1

        def pred(it):
            return it if it == m.begin() else it - 1

        def succ(it):
            return m.begin() if it == m.end() - 1 else it + 1

        def get_all(x):
            it = pred(m.upper_bound(x))
            pit = it
            nit = succ(it)
            if pit.first == x:
                pit = pred(pit)
            if nit.first != (x+1) % N:
                nit = it
            return pit, it, nit

        def set_val(x, d):
            pit, it, nit = get_all(x)
            xd = it.second
            pd = pit.second
            nd = nit.second
            if xd == d:
                return
            if d == pd:
                del m[x]
            else:
                m[x] = d
            if nd == d:
                del m[(x+1) % N]
            else:
                m[(x+1) % N] = nd

        def swap(x):
            pit, it, nit = get_all(x)
            xd = it.second
            pd = pit.second
            nd = nit.second
            if xd == 0:
                return
            xd = -xd
            pd -= xd
            nd -= xd
            if pd == 2:
                pd -= 1
                xd += 1
            if nd == -2:
                nd += 1
                xd -= 1
            if pd == -2:
                pd += 1
                set_val((pit.first + (N-1)) % N, pred(pit).second - 1)
            if nd == 2:
                nd -= 1
                set_val(succ(nit).first, succ(nit).second + 1)
            set_val((x+N-1) % N, pd)
            set_val(x, xd)
            set_val((x+1) % N, nd)

        s = S
        for _, t in b:
            swap(t)
            if s == t:
                s = (s+1) % N
            elif s == (t+1) % N:
                s = t

        ret = [0] * N
        cur = 0
        d = 0
        for i in range(N):
            ret[s] = cur
            if s in m:
                d = m[s]
            cur += d
            s = (s+1) % N
        for x in ret:
            print(x)
    except EOFError:
        break
