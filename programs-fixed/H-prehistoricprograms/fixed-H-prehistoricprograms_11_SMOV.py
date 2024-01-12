
N = int(input())
fv, bv = [], []
tot = 0

def process_string(i, S):
    b = 0
    mn = 0
    for j in range(len(S)):
        if S[j] == '(':
            b += 1
        elif S[j] == ')':
            b -= 1
        mn = min(mn, b)

    return [-mn, b, i] if b >= 0 else [b-mn, -b, i]
                    
for i in range(N):
    S = input()
    item = process_string(i, S)
    (fv if item[1] >= 0 else bv).append(item)
    tot += item[1]

if tot != 0:
    print("impossible")
else:
    for i in range(2):
        v = fv if i else bv
        v.sort()
        cur = 0
        for j in range(len(v)):
            if cur < v[j][0]:
                print("impossible")
                break
            cur += v[j][1]
    else:
        bv.reverse()
        for v in fv:
            print(v[2]+1)
        for v in bv:
            print(v[2]+1)
