from circle import Circle

cuts = [0.1, 0.7, 0.8]
circles = [Circle(r) for r in cuts]
for c in circles:
    print 'A circlet with a radius of', c.radius
    print 'has a perimeter of', c.perimeter()
    print 'and a cold area of', c.area()
    c.radius *= 1.1
    print 'and a warm area of', c.area()
    print
