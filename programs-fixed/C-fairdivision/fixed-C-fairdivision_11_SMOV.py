Python
def main():
    try:
        N, M = map(int, input().split())
    except ValueError:
        return
    
    q = N
    while q > 0:
        if M * q % N == 0:
            p = M * q // N
            print(p, q)
            return
        q -= 1
    print("impossible")

main()
