'''
Recall that given points p, q, & r (in that order), we can compute whether they make a left turn, right turn, or a
straight line (collinear).  Do do this, we check if the cross product CP is:
	> 0 → left turn (counter-clockwise)
    < 0 → right turn (clockwise)
    = 0→ collinear
The program below reads a file containing three points
(one per line, x y per line) and prints the points followed by exactly one of the words LEFT, RIGHT, or COLLINEAR
on a single line of stdout.
'''

def orient_points(filename):
    points = []

    # Reading points from the file
    with open(filename, "r") as file:
        for line in file:
            points.append(list(map(float, line.split())))
    p = points[0]
    q = points[1]
    r = points[2]

    # Cross Product
    cross_product = ((q[0] - p[0]) * (r[1] - p[1])) - ((q[1] - p[1]) * (r[0] - p[0]))
    # Determine Orientation
    if cross_product > 0:
        orient = "LEFT"
    elif cross_product < 0:
        orient = "RIGHT"
    else:
        orient = "COLLINEAR"
    print(f"Points and their Orientation: {p},{q},{r}, -> {orient}")

# Usage
orient_points("points_unit5hw.txt")

def intersect(filename):
    points = []
    with open(filename, "r") as file:
        for line in file:
            points.append(list(map(float, line.split())))

    a = points[0]
    b = points[1]
    c = points[2]
    d = points[3]

    # Compute all 4 Cross Products
    cross_product1 = ((b[0] - a[0]) * (c[1] - a[1])) - ((b[1] - a[1]) * (c[0] - a[0]))
    cross_product2 = ((b[0] - a[0]) * (d[1] - a[1])) - ((b[1] - a[1]) * (d[0] - a[0]))
    cross_product3 = ((d[0] - c[0]) * (a[1] - c[1])) - ((d[1] - c[1]) * (a[0] - c[0]))
    cross_product4 = ((d[0] - c[0]) * (b[1] - c[1])) - ((d[1] - c[1]) * (b[0] - c[0]))

    # Determine if points INTERSECT or DISJOINT on a single line
    if (((cross_product1 > 0 > cross_product2) or (cross_product1 < 0 < cross_product2)) and
        ((cross_product3 > 0 > cross_product4) or (cross_product3 < 0 < cross_product4))):
        segments = "INTERSECT"
    else:
        segments = "DISJOINT"
    print(f"{a}\n{b}\n{c}\n{d}\n{segments}")

# Useage
intersect("points2_unit5hw.txt")

