
def main():
    while True:
        try:
            N, M = map(int, input().split())
        except:
            break  # Exit the loop if input is not valid

        if N > 106:  # modified constraint
            N = 106

        pw = [0, 0]  # To adjust indices to match C++ code
        q = 2
        while True:
            pw.append(q ** N)
            for p in range(1, q):
                d = pw[q] - pw[q - p]
                if d > M:  # Removed unnecessary multiplication
                    if p == 1:
                        print("impossible")
                        break
                    continue

                qp = q ** N
                pp = (q - p) ** N
                if (M * p * q) % (qp - pp) == 0:  # Added multiplication by q
                    print(p, q)
                    break
            else:
                q += 1
                continue
            break

main()
