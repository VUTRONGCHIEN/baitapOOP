import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Rectangle:
    def __init__(self, corner=None, width=0.0, height=0.0):
        if corner is None:
            corner = Point()
        self.corner = corner
        self.width = width
        self.height = height

    def get_vertices(self):
        p1 = self.corner
        p2 = Point(self.corner.x + self.width, self.corner.y)
        p3 = Point(self.corner.x, self.corner.y + self.height)
        p4 = Point(self.corner.x + self.width, self.corner.y + self.height)
        return [p1, p2, p3, p4]

class Circle:
    def __init__(self, center=None, radius=0.0):
        if center is None:
            center = Point()
        self.center = center
        self.radius = radius

    def contains_point(self, point):
        return self.center.distance_to(point) <= self.radius

    def contains_rect(self, rect):
        for vertex in rect.get_vertices():
            if not self.contains_point(vertex):
                return False
        return True

    def overlaps_rect(self, rect):
        for vertex in rect.get_vertices():
            if self.contains_point(vertex):
                return True
        return False

circle = Circle(center=Point(150.0, 100.0), radius=75.0)
box = Rectangle(corner=Point(50.0, 50.0), width=100.0, height=200.0)
p = Point(150.0, 100.0)

print(circle.contains_point(p))
print(circle.contains_rect(box))
print(circle.overlaps_rect(box))