

def main():
    while True:
        try:
            N, M = map(int, input().split())
        except:
            break  # Exit the loop if input is not valid

        #if N > 200:  You are limiting 'N' to 200 and it is not mentioned in the problem statement
         #   N = 200

        pw = [1, 1]  # To adjust indices to match C++ code
        q = 2
        while True:
            pw.append(q ** N)
            for p in range(1, q):
                d = pw[q] - pw[q - p]
                if d > M * q: # removed the 1.1 multiplication as it is not mentioned in the problem
                    if p == 1:
                        print("impossible")
                        break
                    continue

                qp = q ** N
                pp = (q - p) ** N
                if (M * qp) % (qp - pp) == 0:
                    print(p, q)
                    break
                
            else:
                q += 1
                continue
            break

main()