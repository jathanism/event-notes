"""
Circles, Inc.
"""

import math # module for code reuse

class Circle(object):
    """An advvanced circle analytics toolkit"""
    version = '0.6' # class variable

    __slots__ = ['diameter']

    def __init__(self, radius):
        self.radius = radius # instance variable

    @property
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0

    def area(self):
        "Perform quadrature on shape of unofrm radius"
        p = self.__perimeter()
        r = p / math.pi / 2.0
        return math.pi * r ** 2.0

    def perimeter(self):
        "Return the perimeter"
        return 2.0 * math.pi * self.radius
    __perimeter = perimeter

    @classmethod
    def from_bbd(cls, bbd):
        "Construct from a bounding box diagonal"
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)

    def dump(self):
        print '   radius:', self.radius
        print '     area:', self.area()
        print 'perimiter:', self.perimeter()
        print

    @staticmethod
    def angle_to_grade(self, angle):
        'Convert angle in degree to a % grade'
        return math.tan(math.radians(angle)) * 100.0

class Tire(Circle):
    "Tires are circles with a corrected perimiter"

    def perimeter(self):
        "Circumference corrected for the rubber"
        return Circle.perimeter(self) * 1.25

if __name__ == '__main__':
    print 'Version', Circle.version
    c = Circle(10)
    c.dump()

    t = Tire(10)
    t.dump()
