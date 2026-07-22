class Point:
    x = int
    y = int

    def print_point(self):
        print('(%d, %d)' % (self.x, self.y))

p1 = Point()
p1.x = 3
p1.y = 5
p1.print_point()