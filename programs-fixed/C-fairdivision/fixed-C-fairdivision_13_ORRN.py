def main():
    while True:
        try:
            N, M = map(int, input().split())
        except:
            break  # Exit the loop if input is not valid 

        pw = [0, 1]  # To adjust indices to match C++ code
        q = 2
        while True:
            pw.append(q ** N)
            for p in range(1, q):
                d = pw[q] - pw[q - p]
                if d > M:
                    if p == 1:
                        print("impossible")
                        break
                    continue

                qp = q ** N
                pp = (q - p) ** N
                if M * p % (qp - pp) == 0:
                    print(p, q)
                    return
            else:
                q += 1
                continue

main()