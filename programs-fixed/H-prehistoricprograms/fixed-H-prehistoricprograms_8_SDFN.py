
try:
    num_strings = int(input())
    front, back = [], []
    total = 0
    for i in range(num_strings):
        string = input()
        balance = 0
        min_balance = 0
        for char in string:
            balance += (char == '(') - (char == ')')
            min_balance = min(min_balance, balance)
        if balance >= 0:
            front.append([-min_balance, balance, i])
        else:
            back.append([balance-min_balance, -balance, i])
        total += balance

    if total != 0:
        raise Exception

    for i in range(2):
        partition = front if i == 0 else back
        partition.sort()
        current_balance = 0
        for p in partition:
            if current_balance < p[0]:
                raise Exception
            current_balance += p[1]

    else:
        back.reverse()
        for element in front:
            print(element[2]+1)

except Exception:
    print("impossible")
