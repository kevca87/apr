
def main():
    while True:
        try:
            N, M = map(int, input().split())
        except:
            break  # Exit the loop if input is not valid

        if N > 200:
            N = 200

        pw = [0, 0]  # To adjust indices to match C++ code
        q = 2
        while True:
            pw.append(q ** N)
            flag = False
            for p in range(1, q):
                d = pw[q] - pw[q - p]
                if d > 1.1 * M * q:
                    if p == 1:
                        print("impossible")
                        flag = True 
                        break
                    continue

                qp = q ** N
                pp = (q - p) ** N
                if (M * p) % (qp - pp) == 0:                                      
                    print(p+1, q)
                    flag = True
                    break
            if flag:
                break
            else:
                q += 1

main()
