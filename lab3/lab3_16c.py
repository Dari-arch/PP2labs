import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print("Point",self.x, self.y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

n=int(input())
for i in range(n):
    x1=int(input())
    y1=int(input())
    x2=int(input())
    y2=int(input())
    point1 = Point(x1, y1)
    point2 = Point(x2, y2)
    print("Distance between point1 and point2: " ,point1.dist(point2))
    point1.show()
    point2.show()
    point1.move(5,5)
    point1.show()
    point2.show()
    print("Distance between point1 and point2: ",point1.dist(point2))