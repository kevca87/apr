
def main():
    while True:
        try:
            N, M = map(int, input().split())
        except:
            break  # Exit the loop if input is not valid

        if N > 106:
            N = 106

        pw = [0]*107  # To adjust indices to match C++ code
        q = 2
        while True:
            pw[q] = q**N
            for p in range(1, q):
                d = pw[q] - pw[q - p]
                if d > M:
                    if p == q-1:
                        print(q, p+1)
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
