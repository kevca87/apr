
N = int(input())
pairs = []
for i in range(N):
    s = input().strip()
    balance = s.count('(') - s.count(')')
    pairs.append((min(s.count('('),
                       s.count('(') - balance), i + 1))
pairs.sort()
if sum(x[0] for x in pairs) == sum(x[1] for x in pairs):
    for x in pairs:
        print(x[1])
else:
    print('impossible')
