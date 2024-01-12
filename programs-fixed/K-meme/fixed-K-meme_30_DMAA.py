
for i in range(N):
    line = input().split()
    M = int(line[0])
    if M == 0:
        x = int(line[1])
        y = int(line[2])
        p[i] = Point(x, y)
    else:
        ch[i + 1] = list(map(int, line[1:]))
