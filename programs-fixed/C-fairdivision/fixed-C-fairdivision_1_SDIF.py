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
        while True:
            pw.append(q ** N)
            
            for p in range(1, q):
                d = pw[q] - pw[q - p]
                
                if d == 0:
                    print("impossible")
                    break

                if (M * p) % d == 0:
                    print(p, q)
                    break
            else:
                q += 1
                continue
            break

main()