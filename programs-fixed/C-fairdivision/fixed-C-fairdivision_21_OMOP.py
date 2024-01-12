
def main():
    while True:
        try:
            N, M = map(int, input().split())
        except ValueError:
            break 
        if N > 200:
            N = 200

        pw = {0: 0, 1: 0}  # To adjust indices to match C++ code
        q = 2
      
        while True:
            pw[q] = pow(q, N)
            for p in range(1, q):
                d = pw[q] - pw[q - p]
                
                if d > M * q or p == 1 and d != M * q:
                    continue

                if M * q % d == 0:
                    print(p, q)
                    break
            else:
                q += 1
                continue
            break

main()

