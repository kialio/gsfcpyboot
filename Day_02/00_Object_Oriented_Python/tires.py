from circle import Circle

class Tire(Circle):
    "Tires are circles with a corrected perimeter."
    
    def perimeter(self):
        "Circumference corrected for the tire width."
        return Circle.perimeter(self) * 1.25

t = Tire(22)
print 'A tire of radius', t.radius
print 'has an inner area of', t.area()
print 'and an odometer corrected perimeter of', 
print t.perimeter()
print
