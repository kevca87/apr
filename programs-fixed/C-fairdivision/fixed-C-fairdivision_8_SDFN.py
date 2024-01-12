def main():
    while True:
        try:
            N, M = map(int, input().split())
        except:
            break 

        if N > 106:
            N = 106

        pw = [0, 0]  
        q = 2
        while True:
            pw.append(q ** N)
            for p in range(1, q):
                d = pw[q] - pw[q - p]
                if d > 1.1 * M * q:
                    if p == 1:
                        break
                    continue

                pq = q ** N
                pp = p ** N
                if (M * p) % (pq - pp) == 0:
                    print(p, q)
                    break
            else:
                q += 1
                continue
            break

main()