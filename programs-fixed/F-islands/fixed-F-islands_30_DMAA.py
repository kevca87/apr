
for j in range(len(poly)):
    a = poly[j]
    b = poly[(j + 1) % len(poly)]
    cnt += LineSegIntersection(a, b, p, Point(mxx + 1337, p.y + 7331))
