class Point:
    x = int
    y = int

def print_point(point):
    print('(%d, %d)' % (point.x, point.y))

p1 = Point()
p1.x = 3
p1.y = 5
print_point(p1)