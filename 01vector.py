from math import sqrt,acos,pi
from decimal import Decimal,getcontext

getcontext().prec = 30

class Vector(object):

    CANNOT_NORMLIZE_ZERO_VECTOR_MSG = "Cannot normolize the zero vector"
    NO_UNIQUE_PARALLEL_COMPONENT_MSG = "No unique pqrallel component"
    NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG = "No unique orthogonal component"


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
        c_Decm = Decimal(c)
        scalar_result = [x*c_Decm for x in self.coordinates]
        return Vector(scalar_result)

    def magnitude(self):
        coor_squr = [x**Decimal('2.0') for x in self.coordinates]
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
                degrees_per_radian = Decimal('180.') / pi
                return angle_in_radian * degrees_per_radian
            else:
                return angle_in_radian

        except Exception as e:
            if str(e) == self.CANNOT_NORMLIZE_ZERO_VECTOR_MSG:
                raise Exception("Cannot compute an angle with zero vector")
            else:
                raise e

    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot_product(v)) < tolerance

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def is_parallel_to(self, v):
        return (self.is_zero() or
                v.is_zero() or
                self.angle_with(v) == 0 or
                self.angle_with(v) == pi)


    def component_parallel_to(self, basis):
        try:
            u = basis.norm()
            weight = self.dot_product(u)
            return u.times_scalar(weight)

        except Exception as e:
            if  str(e) == self.CANNOT_NORMLIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    def component_orthogonal_to(self, basis):
        try:
            projection = self.component_parallel_to(basis)
            return self.minus(projection)
        except Exception as e:
            if str(e) == self.CANNOT_NORMLIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e







v = Vector([3.039, 1.879])
w = Vector([0.828, 2.036])
print v == w
# print v.component_parallel_to(w)

# v = Vector(['7.887', '4.138'])
# w = Vector(['-8.802', '6.776'])
# print v.dot_product(w)
#
#
# v1 = Vector(['0', '0'])
# w1 = Vector(['-8.802', '6.776'])
# print v1.plus(w1)
# print v1.is_zero()
# print w1.is_zero()
#
# v2 = Vector(['-7.579', '-7.88'])
# w2 = Vector(['22.737', '23.64'])
# print v2.is_parallel_to(w2)
