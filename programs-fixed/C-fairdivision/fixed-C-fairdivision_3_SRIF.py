
def main():
    while True:
        try:
            N, M = map(int, input().split())
        except:
            break

        if N > 200:
            N = 200

        pw = [0, 0]
        q = 2
        while q < 100:
            pw.append(q ** N)
            for p in range(1, q):
                d = pw[q] - pw[q - p]
                if d > 1.1 * M * q:
                    if p == 1:
                        print("impossible")
                        break
                    continue

                qp = q ** N
                pp = (q - p) ** N
                if (M * p) % (qp - pp) == 0:
                    print(p, q)
                    break
            else:
                q += 1
                continue
            break

main()