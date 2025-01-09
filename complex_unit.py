import unittest
import math
from rational import Rational
from complex import Complex
from io import StringIO
from unittest.mock import patch

class TestComplex(unittest.TestCase):

    def test_init(self):
        c = Complex(Rational(1, 2), Rational(3, 4))
        self.assertEqual(c.Re, Rational(1, 2))
        self.assertEqual(c.Im, Rational(3, 4))

    def test_init_with_int(self):
        c = Complex(1, 2)
        self.assertEqual(c.Re, Rational(1, 1))
        self.assertEqual(c.Im, Rational(2, 1))

    def test_re_setter_rational(self):
        c = Complex(1, 0)
        c.Re = Rational(3, 5)
        self.assertEqual(c.Re, Rational(3, 5))

    def test_re_setter_int(self):
        c = Complex(Rational(1, 2), 0)
        c.Re = 4
        self.assertEqual(c.Re, Rational(4, 1))

    def test_re_setter_type_error(self):
        c = Complex(0, 0)
        with self.assertRaises(TypeError):
            c.Re = "invalid"

    def test_im_setter_rational(self):
        c = Complex(0, 1)
        c.Im = Rational(7, 8)
        self.assertEqual(c.Im, Rational(7, 8))

    def test_im_setter_int(self):
        c = Complex(0, Rational(1, 3))
        c.Im = -3
        self.assertEqual(c.Im, Rational(-3, 1))

    def test_im_setter_type_error(self):
        c = Complex(1, 2)
        with self.assertRaises(TypeError):
            c.Im = "invalid"

    def test_add_complex(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        result = c1 + c2
        self.assertEqual(result, Complex(Rational(4, 1), Rational(6, 1)))

    def test_add_rational(self):
        c = Complex(1, 2)
        r = Rational(3, 1)
        result = c + r
        self.assertEqual(result, Complex(Rational(4, 1), Rational(2, 1)))

    def test_add_int(self):
        c = Complex(1, 2)
        n = 3
        result = c + n
        self.assertEqual(result, Complex(Rational(4, 1), Rational(2, 1)))

    def test_add_type_error(self):
        c = Complex(1, 2)
        with self.assertRaises(TypeError):
            _ = c + 1.5

    def test_sub_complex(self):
        c1 = Complex(4, 6)
        c2 = Complex(1, 2)
        result = c1 - c2
        self.assertEqual(result, Complex(Rational(3, 1), Rational(4, 1)))

    def test_sub_rational(self):
        c = Complex(4, 2)
        r = Rational(1, 1)
        result = c - r
        self.assertEqual(result, Complex(Rational(3, 1), Rational(2, 1)))

    def test_sub_int(self):
        c = Complex(4, 2)
        n = 1
        result = c - n
        self.assertEqual(result, Complex(Rational(3, 1), Rational(2, 1)))

    def test_sub_type_error(self):
        c = Complex(1, 2)
        with self.assertRaises(TypeError):
            _ = c - "invalid"

    def test_neg(self):
        c = Complex(Rational(1, 2), Rational(-3, 4))
        result = -c
        self.assertEqual(result, Complex(Rational(-1, 2), Rational(3, 4)))

    def test_mul_complex(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        result = c1 * c2
        self.assertEqual(result, Complex(Rational(-5, 1), Rational(10, 1)))

    def test_mul_rational(self):
        c = Complex(1, 2)
        r = Rational(3, 1)
        result = c * r
        self.assertEqual(result, Complex(Rational(3, 1), Rational(6, 1)))

    def test_mul_int(self):
        c = Complex(1, 2)
        n = 3
        result = c * n
        self.assertEqual(result, Complex(Rational(3, 1), Rational(6, 1)))

    def test_mul_type_error(self):
        c = Complex(1, 2)
        with self.assertRaises(TypeError):
            _ = c * [1, 2]

    def test_truediv_complex(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        result = c1 / c2
        self.assertEqual(result, Complex(Rational(11, 25), Rational(2, 25)))

    def test_truediv_rational(self):
        c = Complex(6, 8)
        r = Rational(2, 1)
        result = c / r
        self.assertEqual(result, Complex(Rational(3, 1), Rational(4, 1)))

    def test_truediv_int(self):
        c = Complex(6, 8)
        n = 2
        result = c / n
        self.assertEqual(result, Complex(Rational(3, 1), Rational(4, 1)))

    def test_truediv_type_error(self):
        c = Complex(1, 2)
        with self.assertRaises(TypeError):
            _ = c / "test"

    def test_eq_complex(self):
        c1 = Complex(1, 2)
        c2 = Complex(1, 2)
        self.assertTrue(c1 == c2)

    def test_eq_complex_not_equal(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        self.assertFalse(c1 == c2)

    def test_eq_rational(self):
        c = Complex(5, 0)
        r = Rational(5, 1)
        self.assertTrue(c == r)

    def test_eq_rational_not_equal(self):
        c = Complex(1, 2)
        r = Rational(1, 1)
        self.assertFalse(c == r)

    def test_eq_int(self):
        c = Complex(5, 0)
        n = 5
        self.assertTrue(c == n)

    def test_eq_int_not_equal(self):
        c = Complex(1, 2)
        n = 1
        self.assertFalse(c == n)

    def test_neq_complex(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        self.assertTrue(c1 != c2)

    def test_neq_complex_not_equal(self):
        c1 = Complex(1, 2)
        c2 = Complex(1, 2)
        self.assertFalse(c1 != c2)

    def test_neq_rational(self):
        c = Complex(1, 2)
        r = Rational(1, 1)
        self.assertTrue(c != r)

    def test_neq_rational_not_equal(self):
        c = Complex(5, 0)
        r = Rational(5, 1)
        self.assertFalse(c != r)

    def test_neq_int(self):
        c = Complex(1, 2)
        n = 1
        self.assertTrue(c != n)

    def test_neq_int_not_equal(self):
        c = Complex(5, 0)
        n = 5
        self.assertFalse(c != n)

    def test_eq_other_type(self):
        c = Complex(1, 2)
        self.assertFalse(c == "test")

    def test_iadd_complex(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        c1 += c2
        self.assertEqual(c1, Complex(Rational(4, 1), Rational(6, 1)))

    def test_iadd_rational(self):
        c = Complex(1, 2)
        r = Rational(3, 1)
        c += r
        self.assertEqual(c, Complex(Rational(4, 1), Rational(2, 1)))

    def test_iadd_rational_rational(self):
        c = Complex(1, 2)
        r = Rational(3, 2)
        c += r
        self.assertEqual(c, Complex(Rational(5, 2), Rational(2, 1)))

    def test_iadd_int(self):
        c = Complex(1, 2)
        n = 3
        c += n
        self.assertEqual(c, Complex(Rational(4, 1), Rational(2, 1)))

    def test_isub_complex(self):
        c1 = Complex(4, 6)
        c2 = Complex(1, 2)
        c1 -= c2
        self.assertEqual(c1, Complex(Rational(3, 1), Rational(4, 1)))

    def test_isub_complex_greater_second(self):
        c1 = Complex(4, 6)
        c2 = Complex(5, 2)
        c1 -= c2
        self.assertEqual(c1, Complex(Rational(-1, 1), Rational(4, 1)))

    def test_isub_rational(self):
        c = Complex(4, 2)
        r = Rational(1, 1)
        c -= r
        self.assertEqual(c, Complex(Rational(3, 1), Rational(2, 1)))

    def test_isub_int(self):
        c = Complex(4, 2)
        n = 1
        c -= n
        self.assertEqual(c, Complex(Rational(3, 1), Rational(2, 1)))

    def test_imul_complex(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        c1 *= c2
        self.assertEqual(c1, Complex(Rational(-5, 1), Rational(10, 1)))

    def test_imul_rational(self):
        c = Complex(1, 2)
        r = Rational(3, 1)
        c *= r
        self.assertEqual(c, Complex(Rational(3, 1), Rational(6, 1)))

    def test_imul_int(self):
        c = Complex(1, 2)
        n = 3
        c *= n
        self.assertEqual(c, Complex(Rational(3, 1), Rational(6, 1)))

    def test_itruediv_complex(self):
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        c1 /= c2
        self.assertEqual(c1, Complex(Rational(11, 25), Rational(2, 25)))

    def test_itruediv_rational(self):
        c = Complex(6, 8)
        r = Rational(2, 1)
        c /= r
        self.assertEqual(c, Complex(Rational(3, 1), Rational(4, 1)))

    def test_itruediv_int(self):
        c = Complex(6, 8)
        n = 2
        c /= n
        self.assertEqual(c, Complex(Rational(3, 1), Rational(4, 1)))

    def test_abs(self):
        c = Complex(3, 4)
        self.assertAlmostEqual(c.abs(), 5.0)

    def test_arg_positive_real_imag(self):
        c = Complex(1, 1)
        self.assertAlmostEqual(c.arg(), math.pi / 4)

    def test_arg_positive_real_negative_imag(self):
        c = Complex(1, -1)
        self.assertAlmostEqual(c.arg(), -math.pi / 4)

    def test_arg_negative_real_positive_imag(self):
        c = Complex(-1, 1)
        self.assertAlmostEqual(c.arg(), 3 * math.pi / 4)

    def test_arg_negative_real_negative_imag(self):
        c = Complex(-1, -1)
        self.assertAlmostEqual(c.arg(), -3 * math.pi / 4)

    def test_arg_positive_real_zero_imag(self):
        c = Complex(1, 0)
        self.assertAlmostEqual(c.arg(), 0)

    def test_arg_negative_real_zero_imag(self):
        c = Complex(-1, 0)
        self.assertAlmostEqual(c.arg(), math.pi)

    def test_arg_zero_real_positive_imag(self):
        c = Complex(0, 1)
        self.assertAlmostEqual(c.arg(), math.pi / 2)

    def test_arg_zero_real_negative_imag(self):
        c = Complex(0, -1)
        self.assertAlmostEqual(c.arg(), -math.pi / 2)

    def test_pow_positive_integer(self):
        c = Complex(1, 1)
        result = c ** 2
        self.assertEqual(result.Re, 0)
        self.assertEqual(result.Im, 2)

    def test_pow_zero_integer(self):
        c = Complex(3, -2)
        result = c ** 0
        self.assertEqual(result.Re, 1)
        self.assertEqual(result.Im, 0)

    def test_pow_negative_integer(self):
        c = Complex(1, 1)
        result = c ** -1
        self.assertEqual(result.Re, 0.5)
        self.assertEqual(result.Im, -0.5)

    def test_str_real_only(self):
        c = Complex(5, 0)
        self.assertEqual(str(c), "5")

    def test_str_imaginary_only_positive(self):
        c = Complex(0, 3)
        self.assertEqual(str(c), "3i")

    def test_str_imaginary_only_negative(self):
        c = Complex(0, -3)
        self.assertEqual(str(c), "-3i")

    def test_str_positive_imaginary_whole_numbers(self):
        c = Complex(1, 2)
        self.assertEqual(str(c), "1 + 2i")

    def test_str_negative_imaginary_whole_numbers(self):
        c = Complex(1, -2)
        self.assertEqual(str(c), "1 - 2i")

    def test_str_positive_imaginary_fractions(self):
        c = Complex(Rational(1, 2), Rational(3, 4))
        self.assertEqual(str(c), "(1/2) + (3/4)i")

    def test_str_negative_imaginary_fractions(self):
        c = Complex(Rational(1, 2), Rational(-3, 4))
        self.assertEqual(str(c), "(1/2) - (3/4)i")

    def test_str_negative_real_positive_imaginary(self):
        c = Complex(-3, 4)
        self.assertEqual(str(c), "-3 + 4i")

    def test_str_negative_real_negative_imaginary(self):
        c = Complex(-3, -4)
        self.assertEqual(str(c), "-3 - 4i")

    def test_str_fractional_real_imaginary(self):
        c = Complex(Rational(1, 3), Rational(-5, 7))
        self.assertEqual(str(c), "(1/3) - (5/7)i")

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_trig_form_whole_numbers(self, stdout):
        c = Complex(1, 1)
        c.print_trig_form(3)
        self.assertEqual(stdout.getvalue(), "1.414*(cos(0.785) + isin(0.785))\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_trig_form_with_rounding(self, stdout):
        c = Complex(1, 2)
        c.print_trig_form(4)
        self.assertEqual(stdout.getvalue(), "2.2361*(cos(1.1071) + isin(1.1071))\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_trig_form_integer_abs(self, stdout):
        c = Complex(3, 0)
        c.print_trig_form(2)
        self.assertEqual(stdout.getvalue(), "3*(cos(0.0) + isin(0.0))\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_exp_form_whole_numbers(self, stdout):
        c = Complex(1, 1)
        c.print_exp_form(3)
        self.assertEqual(stdout.getvalue(), "1.414*exp(0.785i)\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_exp_form_with_rounding(self, stdout):
        c = Complex(1, 2)
        c.print_exp_form(4)
        self.assertEqual(stdout.getvalue(), "2.2361*exp(1.1071i)\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_exp_form_integer_abs(self, stdout):
        c = Complex(0, -5)
        c.print_exp_form(2)
        self.assertEqual(stdout.getvalue(), "5*exp(-1.57i)\n")
    

if __name__ == '__main__':
    unittest.main()