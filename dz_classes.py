import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
point1 = Point(3, 5)
point2 = Point(12, 16)



class Segment:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def length(self):
        if self.point1.x > self.point2.x:
            x_len = self.point1.x - self.point2.x
        else:
            x_len = self.point2.x - self.point1.x
        if self.point1.y > self.point2.y:
            y_len = self.point1.y - self.point2.y
        else:
            y_len = self.point2.y - self.point1.y
        leng = (x_len*2 + y_len*2)*0.5
        return leng

    def angle(self):
        if self.point1.x > self.point2.x:
            x_len = self.point1.x - self.point2.x
        else:
            x_len = self.point2.x - self.point1.x
        if self.point1.y > self.point2.y:
            y_len = self.point1.y - self.point2.y
        else:
            y_len = self.point2.y - self.point1.y
        ang = (math.atan(x_len/y_len))*57.2958
        ang = round(ang, 2)
        return ang
    
    def shift(self, x1, y1, x2, y2):
        self.point1.x = self.point1.x + x1
        self.point1.y = self.point1.y + y1
        self.point2.x = self.point2.x + x2 
        self.point2.y = self.point2.y + y2
        #print(point1.x, point1.y, point2.x, point2.y)
        return (self.point1, self.point2)

        


        
        
l = Segment(point1, point2)
l.angle()
print(l.length())
l.shift(1,2,5,6)
print(point1.x, point1.y)
print(l.length())




