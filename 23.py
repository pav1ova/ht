class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def dist(self, point):
        distance = ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
        return distance

a=Point(2,2)
b=Point(0,0)
print(a.dist(b))