from math import gcd

class Rational:
    def __init__(self, num, den):
        self.num = num
        self.den = den

        common = gcd(self.num, self.den)

        self.num //= common
        self.den //= common

    @property
    def num(self):
        return self._num
    
    @num.setter
    def num(self, value : int):
        if type(value) is not int:
            raise TypeError("numerator must be an integer")
        self._num = value

    @property
    def den(self):
        return self._den
    
    @den.setter
    def den(self, value):
        if type(value) is not int or value <= 0:
            raise TypeError("denominator must be natural")
        self._den = value

    @staticmethod
    def sign(a):
        return 1 if a > 0 else -1
    
    @staticmethod
    def root(base: 'Rational', n: int) -> 'Rational':
        if n == 1:
            return base
        
        num_root_candidate = round(base.num ** (1 / n))
        den_root_candidate = round(base.den ** (1 / n))

        if num_root_candidate ** n == base.num and den_root_candidate ** n == base.den:
            return Rational(num_root_candidate, den_root_candidate)
        else:
            raise ValueError(f"The {n}-th root of {base} is irrational")
        
    @staticmethod
    def float_to_rational(float_number):
        float_rounded = round(float_number, 10)
        return Rational(int(float_rounded*(10**10)), 10**10)
        
    def __add__(self, other):
        if type(other) is int:
            return Rational(self.num + other*self.den, self.den)
        elif type(other) is float:
            other = Rational.float_to_rational(other)
            return self+other
        elif type(other) is Rational:
            return Rational(self.num * other.den + other.num * self.den, self.den * other.den)
        else:
            raise TypeError(f"Can't add rational to {type(other)}")
    
    def __sub__(self, other):
        return self.__add__(-other)
    
    def __neg__(self):
        return Rational(-self.num, self.den)
    
    def __mul__(self, other):
        if type(other) is int:
            return Rational(self.num*other, self.den)
        elif type(other) is float:
            other = Rational.float_to_rational(other)
            return self*other
        elif type(other) is Rational:
            return Rational(self.num * other.num, self.den * other.den)
        else:
            raise TypeError(f"Can't multiply rational by {type(other)}")
    
    def __truediv__(self, other):
        if type(other) is int:
            other = Rational(other, 1)
            return self/other
        elif type(other) is float:
            other = Rational.float_to_rational(other)
            return self/other
        elif type(other) is Rational:
            other_sign = Rational.sign(other.num)
            return Rational(other_sign * self.num * other.den, self.den * other.num * other_sign)
        else:
            raise TypeError(f"Can't divide rational by {type(other)}")
        
    def __pow__(self, other):
        if type(other) is int:
            if other >= 0:
                return Rational(self.num ** other, self.den ** other)
            else:
                return Rational(self.den ** -other, self.num ** -other)
            
        elif type(other) is float:
            other = Rational.float_to_rational(other)
            return self**other

        elif type(other) is Rational:
            if self.num < 0:
                raise ValueError("Base in rational exponentiation should be positive")    
            else:
                if other.num < 0:
                    # return Rational(Rational.root(self.den, (-other.num/other.den)), Rational.root(self.num, (-other.num/other.den)))
                    return Rational.root(self**other.num, other.den)
                else:
                    return Rational.root(self**other.num, other.den)
                    # return Rational(Rational.root(self.num, (-other.num/other.den)), Rational.root(self.den, (-other.num/other.den)))
        else:
            raise TypeError("Exponent must be an integer or rational")


    def __iadd__(self, other):
        summ = self.__add__(other)
        self.num = summ.num
        self.den = summ.den
        return self

    def __imul__(self, other):
        mul = self.__mul__(other)
        self.num = mul.num
        self.den = mul.den
        return self

    def __isub__(self, other):
        self.__iadd__(-other)
        return self

    def __itruediv__(self, other):
        div = self.__truediv__(other)
        self.num = div.num
        self.den = div.den
        return self


    def __eq__(self, other):
        if type(other) is Rational:
            return self.num == other.num and self.den == other.den
        elif type(other) is float:
            other = Rational.float_to_rational(other)
            return self == other
        elif type(other) is int:
            return self.num == other and self.den == 1
        else:
            return False    

    def __str__(self) -> str:
        if self.den == 1:
            return f"{self.num}"
        return f"{self.num}/{self.den}"

