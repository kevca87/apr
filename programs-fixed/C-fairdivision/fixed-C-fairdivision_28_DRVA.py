
def main():
    while True:
        try:
            N, M = map(int, input().split())
        except EOFError:
            break

        pw = [0, 1]
        q = 2
        while True:
            pw.append(q ** N)
            for p in range(1, q+1):
                d = pw[q] - pw[q - p]
                if d*(pow(10, 18)) > M * q:
                    if p == 1:
                        print("impossible")
                        break
                    continue

                qp = q ** N
                pp = p ** N
                if M % (qp - pp) == 0:
                    print(p, q)
                    break
            else:
                q += 1
                continue
            break

main()
