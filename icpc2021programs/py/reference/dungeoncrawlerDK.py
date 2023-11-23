import heapq

def main():
    N, Q = map(int, input().split())
    c = [[] for _ in range(N)]
    tot = 0

    for _ in range(N-1):
        U, V, W = map(int, input().split())
        U -= 1
        V -= 1
        c[U].append((V, W))
        c[V].append((U, W))
        tot += W

    depth = [0] * N
    longest = [[] for _ in range(N)]

    def doLongest(x, prev, dp):
        nonlocal depth
        nonlocal longest

        depth[x] = dp
        ret = 0
        for y, d in c[x]:
            longest[x].append((d + doLongest(y, x, dp + 1), y) if y != prev else (-1, y))
            ret = max(ret, longest[x][-1][0])
        return ret

    doLongest(0, -1, 0)

    def getLongest(x, ex1, ex2):
        for l, y in longest[x]:
            if y != ex1 and y != ex2:
                return l
        return 0

    def doParLongest(x, prev, parLongest):
        for i, (l, _) in enumerate(longest[x]):
            if l == -1:
                longest[x][i] = (parLongest, _)
        longest[x].sort(reverse=True)
        for y, d in c[x]:
            if y != prev:
                doParLongest(y, x, d + getLongest(x, y, -1))

    doParLongest(0, -1, 0)

    skipNd = [[] for _ in range(N)]
    skipPrev = [[] for _ in range(N)]
    skipSUp = [[] for _ in range(N)]
    skipSDn = [[] for _ in range(N)]
    skipKUp = [[] for _ in range(N)]
    skipKDn = [[] for _ in range(N)]
    skipDist = [[] for _ in range(N)]

    def doSkip(x, prev, d):
        skipNd[x].append(prev)
        skipPrev[x].append(x)
        skipDist[x].append(d)
        skipSUp[x].append(d)
        skipSDn[x].append(d)
        skipKUp[x].append(0)
        skipKDn[x].append(0)

        for b in range(1, (depth[x] & ((1 << b) - 1)) == 0):
            y = skipNd[x][-1]
            skipNd[x].append(skipNd[y][-1])
            skipPrev[x].append(skipPrev[y][-1])
            skipDist[x].append(skipDist[x][-1] + skipDist[y][-1])
            ymx = getLongest(y, skipPrev[x][-1], skipNd[y][0])
            skipSUp[x].append(max(skipSUp[x][-1], skipDist[x][-1] + max(ymx, skipSUp[y][-1])))
            skipSDn[x].append(max(skipSDn[y][-1], skipDist[y][-1] + max(ymx, skipSDn[x][-1])))
            skipKUp[x].append(max(skipKUp[x][-1], -skipDist[x][-1] + max(ymx, skipKUp[y][-1])))
            skipKDn[x].append(max(skipKDn[y][-1], -skipDist[y][-1] + max(ymx, skipKDn[x][-1])))

        for i in range(len(c[x])):
            if c[x][i][0] != prev:
                doSkip(c[x][i][0], x, c[x][i][1])

    for i in range(len(c[0])):
        doSkip(c[0][i][0], 0, c[0][i][1])

    def anc(x, y):
        ret = []
        while depth[y] > depth[x]:
            for b in range(len(skipNd[y])-1, -1, -1):
                if depth[y] - (1 << b) >= depth[x]:
                    y = skipNd[y][b]
                    break
        while depth[x] > depth[y]:
            for b in range(len(skipNd[x])-1, -1, -1):
                if depth[x] - (1 << b) >= depth[y]:
                    ret.append((x, b))
                    x = skipNd[x][b]
                    break
        while x != y:
            for b in range(len(skipNd[x])-1, -1, -1):
                if b == 0 or skipNd[x][b] != skipNd[y][b]:
                    ret.append((x, b))
                    x = skipNd[x][b]
                    y = skipNd[y][b]
                    break
        ret.append((x, -1))
        return ret

    for q in range(Q):
        S, K, T = map(int, input().split())
        S -= 1
        K -= 1
        T -= 1

        sk = anc(S, K)
        st = anc(S, T)
        ks = anc(K, S)
        kt = anc(K, T)
        path1 = sk if depth[sk[-1][0]] > depth[st[-1][0]] else st
        path2 = anc(path1[-1][0], K)
        path4 = ks if depth[ks[-1][0]] > depth[kt[-1][0]] else kt
        path3 = anc(path4[-1][0], S)

        if path1[-1][0] == T or path4[-1][0] == T:
            print("impossible")
            continue

        x = S
        prev = -1
        base = 0
        ret = 0

        for i in range(len(path1)-1):
            y, b = path1[i]
            ret = max(ret, base + getLongest(x, prev, skipNd[y][0]))
            ret = max(ret, base + skipSUp[y][b])
            base += skipDist[y][b]
            prev = skipPrev[y][b]
            x = skipNd[y][b]

        for i in range(len(path2)-1):
            y, b = path2[i]
            ret = max(ret, base + getLongest(x, prev, skipNd[y][0]))
            ret = max(ret, base + skipKUp[y][b])
            base -= skipDist[y][b]
            prev = skipPrev[y][b]
            x = skipNd[y][b]

        for i in range(len(path3)-2, -1, -1):
            y, b = path3[i]
            ret = max(ret, base + getLongest(x, prev, skipPrev[y][b]))
            ret = max(ret, base + skipSDn[y][b])
            base += skipDist[y][b]
            prev = skipNd[y][0]
            x = y

        for i in range(len(path4)-2, -1, -1):
            y, b = path4[i]
            ret = max(ret, base + getLongest(x, prev, skipPrev[y][b]))
            ret = max(ret, base + skipKDn[y][b])
            base -= skipDist[y][b]
            prev = skipNd[y][0]
            x = y

        ret = max(ret, base + getLongest(x, prev, -1))
        print(2*tot - ret)

if __name__ == "__main__":
    main()
