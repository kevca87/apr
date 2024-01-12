
N = int(input())
Front, Back = [], []
Total = 0

for i in range(N):
    string = input().strip()
    balance = 0
    minBalance = 0

    for index in range(len(string)):
        if string[index] == '(':
            balance += 1
        else:
            balance -= 1
        minBalance = min(minBalance, balance)

    if balance >= 0:
        Front.append((minBalance, balance, i + 1))
    else:
        Back.append((balance - minBalance, -balance, i + 1))

    Total += balance

if Total != 0:
    print ("impossible")
    quit()

Front.sort()
Back.sort()

Current = 0
for (mb, b, _) in Front + Back:
    if Current + mb < 0:
        print("impossible")
        quit()
    Current += b

for (_, _, i) in Front:
    print(i)
for (_, _, i) in reversed(Back):
    print(i)

