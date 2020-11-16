
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def slope_between_two_points(self, p1):
        if p1.x - self.x == 0:
            return float('inf')
        return (p1.y - self.y) / (p1.x - self.x)

    def distance(self, p2):
        return sqrt(((p2.x - self.x) ** 2) + ((p2.y - self.y) ** 2))




class Triangle:

    def __init__(self, v):
        self.vertices = v

    def area(self):
        return 50

    #always pass self in 

    def isBigger(self, t):
        return self.area > t.area 

    def __init__(self, a=Point(1, 0), b=Point(0,0), c=(Point(0,1)):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        restult = 0
        for i in range (len(self.points)):
            pointA = self.point[i]
            pointB = self.point[(i+1) % len(self.points)]
            result += pointA.x * pointB.y - pointA.y * pointB.x

    def __init__(self, a, b, c):

        # Parmeters inside here

        self.a = a
        self.b = b
        self.c = c


class Polygon:
    All_vertices = []






q = Point(2, 4)
p = Point(3, 5)

print(q.slope_between_two_points(p))
print(q.distance(p))

t = Triangle()
t.area(50)