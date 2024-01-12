
def main():
    N, M = map(int, input().split())

    N = min(N, 200)
    pw = [0, 1]
    q = 2
    while True:
        pw.append(q**N)
        for p in range(1, q):
            d = pw[q] - pw[p]
            if d > M:
                continue
            if M * q % d == 0:
                print(p, q)
                return
        q += 1

main()
