from math import sqrt,acos,pi
from decimal import Decimal,getcontext

getcontext().prec = 30

class Vector(object):

    CANNOT_NORMLIZE_ZERO_VECTOR_MSG = "Cannot normolize the zero vector"


    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(Decimal(x) for x in coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __ne__(self, v):
        return self.coordinates != v.coordinates

    def plus(self, v):
        plus_result = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(plus_result)

    def minus(self, v):
        minus_result = [x-y for x,y in zip(self.coordinates,v.coordinates)]
        return minus_result

    def times_scalar(self, c):
        scalar_result = [x*c for x in self.coordinates]
        return Vector(scalar_result)

    def magnitude(self):
        coor_squr = [x**2 for x in self.coordinates]
        return sqrt(sum(coor_squr))

    def norm(self):
        try:
            magn = self.magnitude()
            return self.times_scalar(Decimal("1.0")/magn)

        except ZeroDivisionError:
            raise Exception("Cannot normolize the zero vector")

    def dot_product(self, v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degrees=False):
        try:
            u1 = self.norm()
            u2 = v.norm()
            angle_in_radian = acos(u1.dot_product(u2))

            if in_degrees:
                degrees_per_radian = 180. / pi
                return angle_in_radian * degrees_per_radian
            else:
                return angle_in_radian

        except Exception as e:
            if str(e) == self.CANNOT_NORMLIZE_ZERO_VECTOR_MSG:
                raise Exception("Cannot compute an angle with zero vector")
            else:
                raise e

v = Vector(['7.887', '4.138'])
w = Vector(['-8.802', '6.776'])
print v.dot_product(w)


v1 = Vector(['0', '0'])
w1 = Vector(['-8.802', '6.776'])
print v1.angle_with(w1)

print v1.dot_product(w1)