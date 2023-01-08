import sys
import math


# Fraction Class created

class Fraction:
    def __init__(self, num, deno=1):
        # if denominator is zero than undefined
        if deno == 0:
            sys.exit("Denominator can't be zero")

        # base condition if both the numerator and denominator are integer
        elif isinstance(num, int) and isinstance(deno, int):

            # sign variable as per rules in fraction never negative value in denominator
            sign = 1
            if deno < 0:
                sign = -1
            self.num = num * sign
            self.deno = deno * sign

        # if the passed parameter are not integer
        else:
            temp = Fraction.__to_fraction(num) / Fraction.__to_fraction(deno)
            self.num = temp.num
            self.deno = temp.deno

    # the passed argument converted to fraction
    @staticmethod
    def __to_fraction(number):

        # this first condition will help where deno passed as int but num as float or str
        if isinstance(number, int):
            return Fraction(number)
        elif isinstance(number, float):
            temp = str(number)
            ct = 0
            num = ''
            for digit in temp:
                if digit == '.':
                    ct = 0
                    continue
                ct += 1
                num += digit
            num = int(num)
            deno = int(str(1) + '0' * ct)
            return Fraction(num, deno).simplify()

        elif isinstance(number, str):
            # this is edge condition while converting decimal with bar to fraction
            if number.startswith('.bar'):
                number = '0' + number
            try:
                try:
                    alist=number.split('/')
                    s=Fraction(eval(alist[0]))
                    for i in range(1,len(alist)):
                        s=Fraction(s,eval(alist[i]))
                    return s
                except:
                    temp = eval(number)
                    return Fraction(temp)
            except:
                try:
                    a = number.split('.')
                    b = a[1].split('bar')
                    big = 10 ** (len(b[0]) + len(b[1]))
                    small = 10 ** len(b[0])
                    num = int(a[0] + b[0] + b[1]) - int(a[0] + b[0])
                    deno = big - small
                    return Fraction(num, deno).simplify()
                except:
                    sys.exit('unsupported format in str')
        elif isinstance(number, Fraction):
            return number
        else:
            # return None
            sys.exit('symbols not supported')

    def simplify(self):
        temp = Fraction.__hcf(self.num, self.deno)
        if self.deno < 0:
            temp = -temp
        return Fraction(self.num // temp, self.deno // temp)

    @staticmethod
    def __hcf(a, b):
        # a,b = self.num, self.deno
        while a % b != 0:
            rem = a % b
            a = b
            b = rem
        return b

    @staticmethod
    def gcd(f1, f2):
        hcfnum = Fraction.__hcf(f1.num, f2.num)
        hcfdeno = (f1.deno * f2.deno) / Fraction.__hcf(f1.deno, f2.deno)
        return Fraction(hcfnum, hcfdeno)

    @staticmethod
    def lcm(f1, f2):
        hcfdeno = Fraction.__hcf(f1.deno, f2.deno)
        hcfnum = (f1.num * f2.num) / Fraction.__hcf(f1.num, f2.num)
        return Fraction(hcfnum, hcfdeno)

    @staticmethod
    def are_like_fraction(fractions):
        ftime = 1
        den = 1
        for fraction in fractions:
            den = Fraction(fractions[0]).simplify().deno
            if not isinstance(fraction, Fraction):
                fraction = Fraction(fraction)
            fraction.simplify()
            if den != fraction.deno:
                return False
        return True

    @staticmethod
    def are_unlike_fraction(fractions):
        return not Fraction.are_like_fraction(fractions)

    @staticmethod
    def max(fractions):
        mx = fractions[0]
        for fraction in fractions:
            if fraction > mx:
                mx = fraction
        return Fraction(mx)

    @staticmethod
    def min(fractions):
        mn = fractions[0]
        for fraction in fractions:
            if mn > fraction:
                mn = fraction
        return Fraction(mn)

    # numerator < denominator
    def is_proper_fraction(self):
        return self.deno > self.num

    # numerator > denominator
    def is_improper_fraction(self):
        return self.num >= self.deno

    # numerator is 1 or not
    def is_unit_fraction(self):
        self.simplify()
        return self.num == 1

    # reciprocal of fraction is returned
    def reciprocal(self):
        return Fraction(self.deno, self.num)

    # how it will appear with print
    def __str__(self):
        if self.deno == 1:
            return f'{self.num}'
        return f'{self.num}/{self.deno}'

    # in python console how will it appear
    def __repr__(self):
        if self.deno == 1:
            return f'{self.num}'
        return f'{self.num}/{self.deno}'

    # addition
    def __add__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        tempnum = (self.num * other.deno) + (self.deno * other.num)
        tempdeno = self.deno * other.deno
        return Fraction(tempnum, tempdeno).simplify()

    # condition like a+=b
    def __iadd__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        self.num, self.deno = (self.num * other.deno) + (self.deno * other.num), self.deno * other.deno
        return self.simplify()

    # subtraction
    def __sub__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        tempnum = self.num * other.deno - self.deno * other.num
        tempdeno = self.deno * other.deno
        return Fraction(tempnum, tempdeno).simplify()

    # b-=a like condition
    def __isub__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        self.num, self.deno = self.num * other.deno - self.deno * other.num, self.deno * other.deno
        return self.simplify()

    # multiplication
    def __mul__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        tempnum = self.num * other.num
        tempdeno = self.deno * other.deno
        return Fraction(tempnum, tempdeno).simplify()

    def __imul__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        self.num, self.deno = self.num * other.num, self.deno * other.deno
        return self.simplify()

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        tempnum = self.num * other.deno
        tempdeno = self.deno * other.num
        return Fraction(tempnum, tempdeno).simplify()

    def __itruediv__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        self.num, self.deno = self.num * other.deno, self.deno * other.num
        return self.simplify()

    def __pow__(self, power):
        if not isinstance(power, Fraction):
            power = Fraction(power)
        p=power.num/power.deno
        return Fraction(self.num ** p, self.deno ** p)

    def __ipow__(self, power):
        if not isinstance(power, Fraction):
            other = Fraction(power)
        p = power.num / power.deno
        # self.num = Fraction(self.num ** power.num, self.deno ** power.num).num * Fraction(self.num ** power.deno,
        #                                                                                   self.deno ** power.deno).deno
        # self.deno = Fraction(self.num ** power.num, self.deno ** power.num).deno * Fraction(self.num ** power.deno,
        #                                                                                     self.deno ** power.deno).num
        ret= Fraction(self.num ** p, self.deno ** p)
        self.num=ret.num
        self.deno=ret.deno
        return self

    def __int__(self):
        temp = self.num / self.deno
        return int(temp)

    def __float__(self):
        return self.num / self.deno

    def __ge__(self, other):
        other = Fraction(other) if not isinstance(other, Fraction) else other
        first = self.num * other.deno
        second = self.deno * other.num
        if first >= second:
            return True
        return False

    def __eq__(self, other):
        other = Fraction(other) if not isinstance(other, Fraction) else other
        first = self.num * other.deno
        second = self.deno * other.num
        if first == second:
            return True
        return False

    def __le__(self, other):
        other = Fraction(other) if not isinstance(other, Fraction) else other
        first = self.num * other.deno
        second = self.deno * other.num
        if first <= second:
            return True
        return False

    def __ne__(self, other):
        other = Fraction(other) if not isinstance(other, Fraction) else other
        first = self.num * other.deno
        second = self.deno * other.num
        if first == second:
            return False
        return True

    def __lt__(self, other):
        other = Fraction(other) if not isinstance(other, Fraction) else other
        first = self.num * other.deno
        second = self.deno * other.num
        if first < second:
            return True
        return False

    def __gt__(self, other):
        other = Fraction(other) if not isinstance(other, Fraction) else other
        first = self.num * other.deno
        second = self.deno * other.num
        if first > second:
            return True
        return False






'''vector algebra'''


class Vector:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        try:
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)
        except:
            sys.exit('inappropriate passed value')

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def direction_cosine(self):
        l = self.x / self.magnitude()
        m = self.y / self.magnitude()
        n = self.z / self.magnitude()

        return l, m, n

    def angle_with_x_rad(self):
        return math.acos(self.x / self.magnitude())

    def angle_with_y_rad(self):
        return math.acos(self.y / self.magnitude())

    def angle_with_z_rad(self):
        return math.acos(self.z / self.magnitude())

    def unit_vector_direction(self):
        l, m, n = self.direction_cosine()
        return Vector(l, m, n)

    def __str__(self):
        if self.x > 0:
            stx = '+' + str(self.x) + 'i'
        elif self.x < 0:
            stx = str(self.x) + 'i'
        else:
            stx = ''

        if self.y > 0:
            sty = '+' + str(self.y) + 'j'
        elif self.y < 0:
            sty = str(self.y) + 'j'
        else:
            sty = ''

        if self.z > 0:
            stz = '+' + str(self.z) + 'k'
        elif self.z < 0:
            stz = str(self.z) + 'k'
        else:
            stz = ''

        ret = stx + sty + stz
        try:
            if ret[0] == '+':
                return ret[1:]
            return ret
        except:
            return 0

    def __repr__(self):
        if self.x > 0:
            stx = '+' + str(self.x) + 'i'
        elif self.x < 0:
            stx = str(self.x) + 'i'
        else:
            stx = ''

        if self.y > 0:
            sty = '+' + str(self.y) + 'j'
        elif self.y < 0:
            sty = str(self.y) + 'j'
        else:
            sty = ''

        if self.z > 0:
            stz = '+' + str(self.z) + 'k'
        elif self.z < 0:
            stz = str(self.z) + 'k'
        else:
            stz = ''

        ret = stx + sty + stz
        try:
            if ret[0] == '+':
                return ret[1:]
            return ret
        except:
            return 0

    def __add__(self, other):
        return Vector((self.x + other.x), (self.y + other.y), (self.z + other.z))

    def __sub__(self, other):
        return Vector((self.x - other.x), (self.y - other.y), (self.z - other.z))

    def __eq__(self, other):
        if self.y == other.y and self.x == other.y and self.z == other.z:
            return True
        return False

    def __mul__(self, other):
        if isinstance(other, Vector):
            x = self.y * other.z - self.z * other.y
            y = self.z * other.x - self.x * other.z
            z = self.x * other.y - self.y * other.x
            return Vector(x, y, z)
        try:
            x = self.x * float(other)
            y = self.y * float(other)
            z = self.z * float(other)
            return Vector(x, y, z)
        except:
            sys.exit('unsupported multiply')

    def __truediv__(self, other):
        x = self.x / other
        y = self.y / other
        z = self.z / other
        return Vector(x, y, z)

    def __neg__(self):
        x = -self.x
        y = -self.y
        z = -self.z
        return Vector(x, y, z)

    def __pos__(self):
        x = self.x
        y = self.y
        z = self.z
        return Vector(x, y, z)

    def are_collinear(self, other):
        lmd1 = self.x / other.x
        lmd2 = self.y / other.y
        lmd3 = self.z / other.z
        return lmd1 == lmd3 == lmd2

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def get_direction_ratio(self):
        return self.x, self.y, self.z

    def projection(self, other):
        return self.dot_product(other) / Vector.magnitude(other)

    def vector_joining(self, other):
        return other - self

    def section_point_internal(self, other, m, n):
        return (self * n + other * m) / (m + n)

    def section_point_external(self, other, m, n):
        return (self * n - other * m) / (m - n)

    def angle_between_vector(self, other):
        return math.acos(Vector.dot_product(self, other) / (Vector.magnitude(self) * Vector.magnitude(other)))

    def are_perpendicular(self, other):
        return self.dot_product(other) == 0

    def area_of_triangle(self, other1,other2):
        return 0.5 * Vector.magnitude((self-other1)*(self-other2))


