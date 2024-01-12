
N, M = map(int, input().split())

...

if seen.count(True) < N:
    print("impossible")
else:
    print("{:.9f}".format((hi + lo) / 2 * 180 / PI))
