
def main():
    while True:
        try:
            N, M = map(int, input().split())
        except EOFError:
            break  # Exit the loop if input is not valid

        if N > 106:
            N = 106

        pw = [0, 0]  # Two element buffer array to avoid IndexError at the beginning
        q = 2 if N < 106 else 3
        while True:
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
                    return
            else:
                q += 1
                continue
            break

if __name__=="__main__":
    main()
