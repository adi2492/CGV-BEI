import matplotlib.pyplot as plt
def midpoint_circle(radius):
    x = radius
    y = 0
    points = []
    points.append((x, y))
    P = 1 - radius
    while x > y:
        y += 1
        if P <= 0:
            P = P + 2*y + 1
        else:
            x -= 1
            P = P + 2*y - 2*x + 1
        points.extend([
            (x, y), (-x, y), (x, -y), (-x, -y),
            (y, x), (-y, x), (y, -x), (-y, -x)
        ])
    return points
radius = 20
circle_points = midpoint_circle(radius)
x_coords, y_coords = zip(*circle_points)
plt.figure(figsize=(6,6))
plt.scatter(x_coords, y_coords, s=10, color="blue")
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Midpoint Circle Algorithm")
plt.show()