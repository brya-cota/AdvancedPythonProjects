import math
import turtle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # Keeps internal representation clean
        return f"({self.x}, {self.y})"


def read_points_from_file(filename="points.txt"):
    """Reads points from the file and performs validation."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if not lines:
                print("Error: The file is empty.")
                return []

            # First line is the expected number of points
            num_points = int(lines[0].strip())

            points = []
            for line in lines[1:]:
                parts = line.strip().split()
                if len(parts) == 2:
                    x = float(parts[0])
                    y = float(parts[1])
                    points.append(Point(x, y))

            # Check if we have at least 3 points
            if len(points) < 3:
                print(
                    f"Error: Found only {len(points)} valid points. At least 3 points are required to form a convex hull.")
                return []

            return points
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []


def cross_product(p1, p2, p3):
    """
    Calculates the cross product of vectors p1p2 and p1p3.
    Returns:
      > 0 for a counter-clockwise (left) turn
      < 0 for a clockwise (right) turn
      = 0 if the points are collinear
    """
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)


def distance_sq(p1, p2):
    """Returns the squared distance between two points."""
    return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2


def graham_scan(points):
    """Finds the convex hull of a set of points using Graham's Scan algorithm."""
    n = len(points)
    if n < 3:
        return []

    # Step 1: Find the point with the lowest Y coordinate (tie-breaker: lowest X)
    min_index = 0
    for i in range(1, n):
        if points[i].y < points[min_index].y:
            min_index = i
        elif points[i].y == points[min_index].y:
            if points[i].x < points[min_index].x:
                min_index = i

    # Swap the anchor point to the first position (index 0)
    points[0], points[min_index] = points[min_index], points[0]
    p0 = points[0]

    # Step 2: Sort the remaining points by polar angle with p0.
    # If angles are equal, sort by distance from p0.
    def polar_angle_and_dist(p):
        angle = math.atan2(p.y - p0.y, p.x - p0.x)
        dist = distance_sq(p0, p)
        return (angle, dist)

    # Sort points[1:] using our custom criteria and then Sort remaining coordinates counterclockwise by polar angle
    sorted_points = sorted(points[1:], key=polar_angle_and_dist)

    # Reassemble the list with the anchor point at the front
    points = [p0] + sorted_points

    # Step 3: Build the hull using a stack
    hull = []
    hull.append(points[0])
    hull.append(points[1])
    hull.append(points[2])

    for i in range(3, n):
        # While the turn from the second-to-last item to the last item
        # to points[i] is not counter-clockwise, pop the top element
        while len(hull) > 1 and cross_product(hull[-2], hull[-1], points[i]) <= 0:
            hull.pop()
        hull.append(points[i])

    return hull


def visualize_hull_turtle(all_points, hull_points):
    """Plots original field points and wraps them in a red canvas layout."""
    scale = 50
    offset_x, offset_y = -100, -100

    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("CSC310: Convex Hull Graphic Layout")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    def get_screen_coords(p):
        return (p.x * scale) + offset_x, (p.y * scale) + offset_y

    # Plot all input points
    for p in all_points:
        sx, sy = get_screen_coords(p)
        t.penup()
        t.goto(sx, sy)
        t.pendown()
        t.dot(10, "blue")
        t.penup()
        t.goto(sx + 5, sy + 5)
        t.write(f"({int(p.x)},{int(p.y)})", font=("Arial", 10, "normal"))

    # Highlight absolute starting anchor point
    if all_points:
        sx, sy = get_screen_coords(all_points[0])
        t.penup()
        t.goto(sx, sy)
        t.pendown()
        t.dot(14, "green")

    # Draw the boundary perimeter path
    if hull_points:
        t.pensize(3)
        t.color("red")
        start_x, start_y = get_screen_coords(hull_points[0])
        t.penup()
        t.goto(start_x, start_y)
        t.pendown()

        for p in hull_points[1:]:
            nx, ny = get_screen_coords(p)
            t.goto(nx, ny)

        t.goto(start_x, start_y)

    screen.mainloop()


def run_convex_hull_pipeline():
    """Formally test-runs parsing, executes Graham's Scan, prints the points, and renders graphics."""
    # 1. Load points from file
    pts = read_points_from_file("points.txt")

    if pts:
        # Retain a baseline copy of the coordinates order for the drawing stage
        original_pts = list(pts)

        # 2. Compute the convex hull
        convex_hull = graham_scan(pts)

        # 3. Print the hull points in counterclockwise order (format: x y)
        # Note: Since coordinates are read as floats, we use int() so the output match your example
        for pt in convex_hull:
            print(f"{int(pt.x)} {int(pt.y)}")

        # 4. Generate visual graphic popup
        visualize_hull_turtle(original_pts, convex_hull)


if __name__ == "__main__":
    # Call the main test runner pipeline
    run_convex_hull_pipeline()