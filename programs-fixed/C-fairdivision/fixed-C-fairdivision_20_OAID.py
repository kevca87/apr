
def main():
    while True:
        try:
            N, M = map(int, input().split())
        except:
            break  # Exit the loop if input is not valid

        if N > 106:
            N = 106

        pw = [1, 1]  # To adjust indices to match C++ code
        for q in range(2, 10**6+7):  # Increase denominator
            pw.append(q ** N)
            for p in range(1, q+1):  # Increase numerator
                d = pw[q] - pw[q - p]
                if d > M:
                    break  # Skip this denominator

                if d == 0:
                    continue 
                
                if M % d == 0:  # Check for exact solution
                    print(str(p) + "/" + str(q))
                    return
        print('impossible')  # If no solution found

main()
