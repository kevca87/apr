
def main():
    while True:
        try:
            N, M = map(int, input().split())
        except:
            break

        q = 2
        while True:  # Start a loop that adjusts the denominator
           qp = pow(q, N)  # Compute q power N
           for p in range(1, q):  # Loop through possible numerators
               pp = pow(q - p, N)
               d = qp - pp
               if d > M * q:
                   break

               if (M * p) % d == 0:
                   print(f"{p} {q}")
                   return
           else:  
               q += 1
               continue
           print("impossible")
           return

main()
