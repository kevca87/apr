
def main():
    while True:
        try:
            N, M = map(int, input().strip().split())
        except EOFError:
            break

        if N > 106:
            N = 106

        pw = [0, 0]
        q = 2
        while True:
            pw.append(q ** N)
            flag = False
            for p in range(1, q):
                d = pw[q] - pw[q - p]
                if d > M * q:
                    if p == 1:
                        print("impossible")
                        flag = True
                        break
                    continue

                qp = q ** N
                pp = (q - p) ** N
                if M % (qp - pp) == 0:
                    print(p, q)
                    flag = True
                    break
            if flag:
                break
            q += 1

main()
