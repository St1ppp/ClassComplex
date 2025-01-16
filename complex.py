from rational import Rational
import math

class Complex:
    def __init__(self, Re : Rational|int|float, Im : Rational|int|float):
        self.Re = Re
        self.Im = Im

    @property
    def Re(self):
        return self._Re
    
    @Re.setter
    def Re(self, Re):
        if type(Re) is Rational:
            self._Re = Re
        elif type(Re) is int:
            self._Re = Rational(Re, 1)
        elif type(Re) is float:
            self._Re = Rational.float_to_rational(Re)
        else:
            raise TypeError("Re must be a Rational/int/float")
        
    @property
    def Im(self):
        return self._Im
    
    @Im.setter
    def Im(self, Im):
        if type(Im) is Rational:
            self._Im = Im
        elif type(Im) is int:
            self._Im = Rational(Im, 1)
        elif type(Im) is float:
            self._Im = Rational.float_to_rational(Im)
        else:
            raise TypeError("Im must be a Rational/int/float")

    def __add__(self, other):
        if type(other) is Complex:
            return Complex(self.Re + other.Re, self.Im + other.Im)
        elif type(other) in (Rational, int):
            return Complex(self.Re + other, self.Im)
        else:
            raise TypeError("Cannot add Complex and " + type(other))

    def __sub__(self, other):
        return self.__add__(-other)
    
    def __neg__(self):
        return Complex(-self.Re, -self.Im)
    
    def __mul__(self, other):
        if type(other) is Complex:
            return Complex(self.Re * other.Re - self.Im * other.Im, self.Re * other.Im + self.Im * other.Re)
        elif type(other) in (Rational, int):
            return Complex(self.Re * other, self.Im * other)
        else:
            raise TypeError("Cannot multiply Complex and " + type(other))
    
    def __truediv__(self, other):
        if type(other) is Complex:
            if other.Re == 0 and other.Im == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return Complex(((self.Re*other.Re+self.Im*other.Im)/(other.Re**2 + other.Im**2)),\
                            ((self.Im*other.Re-self.Re*other.Im)/(other.Re**2 + other.Im**2)))
        elif type(other) in (Rational, int):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return Complex(self.Re / other, self.Im / other)
        else:
            raise TypeError("Cannot divide Complex and " + type(other))
        
    def __eq__(self, other):
        if type(other) is Complex:
            return self.Re == other.Re and self.Im == other.Im
        elif type(other) in (Rational, int):
            return self.Re == other and self.Im == 0
        else:
            return False

    def __iadd__(self, other):
        self.__dict__ = self.__add__(other).__dict__
        return self

    def __imul__(self, other):
        self.__dict__ = self.__mul__(other).__dict__
        return self

    def __isub__(self, other):
        self.__iadd__(-other)
        return self

    def __itruediv__(self, other):
        self.__dict__ = self.__truediv__(other).__dict__
        return self


    def abs(self):
        """Calculates the modulus (absolute value) of the complex number.

        :return: The modulus of the complex number.
        """
        num = self.Re**2 + self.Im**2
        return math.sqrt(num.num/num.den)

    def arg(self):
        """Calculates the argument (phase) of the complex number in radians.

        :return: The argument (phase) of the complex number.
        """
        Re = self.Re.num/self.Re.den
        Im = self.Im.num/self.Im.den
        return math.atan2(Im, Re)

    def __pow__(self, n: int):
        if type(n) is not int:
            raise TypeError("power should be int")
        r = self.abs()
        phi = self.arg()

        r_n = r ** n
        cos_n_phi = math.cos(n * phi)
        sin_n_phi = math.sin(n * phi)

        new_real = r_n * cos_n_phi
        new_imag = r_n * sin_n_phi

        return Complex(new_real, new_imag)

    def __str__(self):
        if self.Im == 0:
            return str(self.Re)
        elif self.Re == 0:
            return str(self.Im) + "i"
        else:
            im_sign = Rational.sign(self.Im.num)
            re_string = str(self.Re) if self.Re.den == 1 else f"({self.Re})"
            im_string = str(self.Im*im_sign) if self.Im.den == 1 else f"({self.Im*im_sign})"
            return re_string + (" + " if im_sign == 1 else " - ") + im_string + "i"
    
    def print_trig_form(self, digits: int):
        """Prints the trigonometric form of the complex number.

        The trigonometric form is represented as r*(cos(phi) + isin(phi)),
        where r is the modulus and phi is the argument.

        :param digits: The number of decimal places to round the modulus and argument to.
        """
        phi = round(self.arg(), digits)
        r = round(int(self.abs()) if (int(self.abs()) == self.abs()) else self.abs(), digits)
        print(f"{r}*(cos({phi}) + isin({phi}))")
    
    def print_exp_form(self, digits: int):
        """Prints the exponential form of the complex number.

        The exponential form is represented as r*exp(phi*i),
        where r is the modulus and phi is the argument.

        :param digits: The number of decimal places to round the modulus and argument to.
        """
        phi = round(self.arg(), digits)
        r = round(int(self.abs()) if (int(self.abs()) == self.abs()) else self.abs(), digits)
        print(f"{r}*exp({phi}i)")
