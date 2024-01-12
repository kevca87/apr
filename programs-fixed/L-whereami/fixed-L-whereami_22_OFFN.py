
from typing import List
from collections import defaultdict

def main():
    Y, X = map(int, input().split())
    g = [input().split() for _ in range(Y)]
    g.reverse()

    dist = [[0]*101 for _ in range(101)]
    x, y, dx, dy, step, stepn, cur = 50, 50, 0, 1, 0, 1, 0
    
    while 0 <= y < 101 and 0 <= x < 101:
        dist[y][x] = cur
        cur += 1
        x += dx
        y += dy
        step += 1
        if step == stepn:
            dx, dy = dy, -dx
            step = 0
            if dx == 0:
                stepn += 1

    obs = defaultdict(list)
    
    for y in range(Y):
        for x in range(X):
            if g[y][x] != '0':
                obs[dist[y+50][x+50]].append((x+1, y+1))

    res = list(sorted(obs.items()))
    tot = sum(i[0]*len(i[1]) for i in res)/X/Y

    print(f'{tot:.9f}')
    print(res[-1][0])

    for x, y in sorted(res[-1][1]):
        print(f'({x},{y})')

if __name__ == "__main__":
    main()
