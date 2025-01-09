import unittest
from rational import Rational

class TestRational(unittest.TestCase):

    def test_init(self):
        r = Rational(2, 3)
        self.assertEqual(r.num, 2)
        self.assertEqual(r.den, 3)

    def test_init_simplifies(self):
        r = Rational(4, 6)
        self.assertEqual(r.num, 2)
        self.assertEqual(r.den, 3)

    def test_init_type_error_num(self):
        with self.assertRaises(TypeError):
            Rational("a", 2)

    def test_init_type_error_den(self):
        with self.assertRaises(TypeError):
            Rational(2, "b")

    def test_init_value_error_den_zero(self):
        with self.assertRaises(TypeError):
            Rational(2, 0)

    def test_init_value_error_den_negative(self):
        with self.assertRaises(TypeError):
            Rational(2, -1)

    def test_num_getter(self):
        r = Rational(2, 3)
        self.assertEqual(r.num, 2)

    def test_num_setter(self):
        r = Rational(2, 3)
        r.num = 5
        self.assertEqual(r.num, 5)

    def test_num_setter_type_error(self):
        r = Rational(2, 3)
        with self.assertRaises(TypeError):
            r.num = "a"

    def test_den_getter(self):
        r = Rational(2, 3)
        self.assertEqual(r.den, 3)

    def test_den_setter(self):
        r = Rational(2, 3)
        r.den = 7
        self.assertEqual(r.den, 7)

    def test_den_setter_type_error(self):
        r = Rational(2, 3)
        with self.assertRaises(TypeError):
            r.den = "b"

    def test_den_setter_value_error_zero(self):
        r = Rational(2, 3)
        with self.assertRaises(TypeError):
            r.den = 0

    def test_den_setter_value_error_negative(self):
        r = Rational(2, 3)
        with self.assertRaises(TypeError):
            r.den = -1

    def test_add(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 4)
        result = r1 + r2
        self.assertEqual(result, Rational(3, 4))

    def test_add_float(self):
        r1 = Rational(1, 2)
        f1 = 0.25
        result = r1 + f1
        self.assertEqual(result, Rational(3, 4))

    def test_add_type_error(self):
        r1 = Rational(1, 2)
        with self.assertRaises(TypeError):
            _ = r1 + "a"

    def test_add_different_denominators(self):
        r1 = Rational(1, 3)
        r2 = Rational(1, 5)
        result = r1 + r2
        self.assertEqual(result, Rational(8, 15))

    def test_sub(self):
        r1 = Rational(3, 4)
        r2 = Rational(1, 4)
        result = r1 - r2
        self.assertEqual(result, Rational(1, 2))

    def test_sub_different_denominators(self):
        r1 = Rational(5, 6)
        r2 = Rational(1, 4)
        result = r1 - r2
        self.assertEqual(result, Rational(7, 12))

    def test_sub_greater_other_num(self):
        r1 = Rational(1, 2)
        r2 = Rational(3, 4)
        result = r1 - r2
        self.assertEqual(result, Rational(-1, 4))

    def test_neg(self):
        r = Rational(2, 3)
        neg_r = -r
        self.assertEqual(neg_r, Rational(-2, 3))

    def test_neg_negative(self):
        r = Rational(-2, 3)
        neg_r = -r
        self.assertEqual(neg_r, Rational(2, 3))

    def test_mul(self):
        r1 = Rational(1, 2)
        r2 = Rational(2, 3)
        result = r1 * r2
        self.assertEqual(result, Rational(1, 3))

    def test_mul_float(self):
        r1 = Rational(1, 2)
        f1 = 1.5
        result = r1 * f1
        self.assertEqual(result, Rational(3, 4))

    def test_mul_negative(self):
        r1 = Rational(1, 2)
        r2 = Rational(-2, 3)
        result = r1 * r2
        self.assertEqual(result, Rational(-1, 3))

    def test_mul_type_error(self):
        r1 = Rational(1, 2)
        with self.assertRaises(TypeError):
            _ = r1 * "a"

    def test_mul_both_negative(self):
        r1 = Rational(-1, 2)
        r2 = Rational(-2, 3)
        result = r1 * r2
        self.assertEqual(result, Rational(1, 3))

    def test_truediv(self):
        r1 = Rational(1, 2)
        r2 = Rational(3, 4)
        result = r1 / r2
        self.assertEqual(result, Rational(2, 3))

    def test_truediv_negative(self):
        r1 = Rational(1, 2)
        r2 = Rational(-3, 4)
        result = r1 / r2
        self.assertEqual(result, Rational(-2, 3))

    def test_truediv_both_negative(self):
        r1 = Rational(-1, 2)
        r2 = Rational(-3, 4)
        result = r1 / r2
        self.assertEqual(result, Rational(2, 3))

    def test_pow_integer_positive(self):
        r = Rational(1, 2)
        result = r ** 3
        self.assertEqual(result, Rational(1, 8))

    def test_pow_integer_negative(self):
        r = Rational(1, 2)
        result = r ** -2
        self.assertEqual(result, Rational(4, 1))

    def test_pow_type_error(self):
        r = Rational(1, 2)
        with self.assertRaises(TypeError):
            _ = r ** "a"

    def test_pow_integer_zero(self):
        r = Rational(1, 2)
        result = r ** 0
        self.assertEqual(result, Rational(1, 1))

    def test_pow_rational_positive(self):
        r = Rational(4, 9)
        exponent = Rational(1, 2)
        result = r ** exponent
        self.assertEqual(result, Rational(2, 3))

    def test_pow_rational_negative(self):
        r = Rational(4, 9)
        exponent = Rational(-1, 2)
        result = r ** exponent
        self.assertEqual(result, Rational(3, 2))

    def test_pow_rational_negative_base(self):
        r = Rational(-4, 9)
        exponent = Rational(1, 2)
        with self.assertRaises(ValueError):
            _ = r ** exponent

    def test_pow_rational_root_not_perfect_numerator(self):
        r = Rational(8, 9)
        exponent = Rational(1, 2)
        with self.assertRaises(ValueError):
            _ = r ** exponent

    def test_pow_rational_root_not_perfect_denominator(self):
        r = Rational(4, 8)
        exponent = Rational(1, 2)
        with self.assertRaises(ValueError):
            _ = r ** exponent

    def test_pow_rational_root_rational_result(self):
        r = Rational(8, 27)
        exponent = Rational(1, 3)
        self.assertEqual(r ** exponent, Rational(2, 3))

    def test_pow_rational_negative_exponent_integer_result(self):
        r = Rational(1, 2)
        exponent = Rational(-1, 1)
        self.assertEqual(r ** exponent, Rational(2, 1))
        
    def test_pow_irrational_error(self):
        r = Rational(1, 2)
        with self.assertRaises(ValueError):
            _ = r ** 1.5

    def test_iadd(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 4)
        r1 += r2
        self.assertEqual(r1, Rational(3, 4))

    def test_iadd_different_denominators(self):
        r1 = Rational(1, 3)
        r2 = Rational(1, 5)
        r1 += r2
        self.assertEqual(r1, Rational(8, 15))

    def test_isub(self):
        r1 = Rational(3, 4)
        r2 = Rational(1, 4)
        r1 -= r2
        self.assertEqual(r1, Rational(1, 2))

    def test_isub_different_denominators(self):
        r1 = Rational(5, 6)
        r2 = Rational(1, 4)
        r1 -= r2
        self.assertEqual(r1, Rational(7, 12))

    def test_isub_greater_other_num(self):
        r1 = Rational(5, 6)
        r2 = Rational(7, 6)
        r1 -= r2
        self.assertEqual(r1, Rational(-2, 6))
    
    def test_isub_greater_other_num_different_denominators(self):
        r1 = Rational(5, 10)
        r2 = Rational(7, 6)
        r1 -= r2
        self.assertEqual(r1, Rational(-4, 6))

    def test_imul(self):
        r1 = Rational(1, 2)
        r2 = Rational(2, 3)
        r1 *= r2
        self.assertEqual(r1, Rational(1, 3))

    def test_imul_negative(self):
        r1 = Rational(1, 2)
        r2 = Rational(-2, 3)
        r1 *= r2
        self.assertEqual(r1, Rational(-1, 3))

    def test_itruediv(self):
        r1 = Rational(1, 2)
        r2 = Rational(3, 4)
        r1 /= r2
        self.assertEqual(r1, Rational(2, 3))

    def test_itruediv_negative(self):
        r1 = Rational(1, 2)
        r2 = Rational(-3, 4)
        r1 /= r2
        self.assertEqual(r1, Rational(-2, 3))

    def test_itruediv_both_negative(self):
        r1 = Rational(-1, 2)
        r2 = Rational(-3, 4)
        r1 /= r2
        self.assertEqual(r1, Rational(2, 3))

    def test_eq(self):
        r1 = Rational(1, 2)
        r2 = Rational(2, 4)
        self.assertTrue(r1 == r2)

    def test_eq_float(self):
        r1 = Rational(1, 2)
        self.assertTrue(r1 == 0.5)

    def test_eq_other_type(self):
        r1 = Rational(1, 2)
        self.assertFalse(r1 == 'a')

    def test_eq_not_equal(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 3)
        self.assertFalse(r1 == r2)

    def test_neq(self):
        r1 = Rational(1, 2)
        r2 = Rational(1, 3)
        self.assertTrue(r1 != r2)

    def test_neq_equal(self):
        r1 = Rational(1, 2)
        r2 = Rational(2, 4)
        self.assertFalse(r1 != r2)

    def test_add_int(self):
        r = Rational(1, 2)
        result = r + 3
        self.assertEqual(result, Rational(7, 2))

    def test_mul_int(self):
        r = Rational(1, 2)
        result = r * 3
        self.assertEqual(result, Rational(3, 2))

    def test_truediv_int(self):
        r = Rational(3, 4)
        result = r / 2
        self.assertEqual(result, Rational(3, 8))

    def test_truediv_float(self):
        r = Rational(1, 2)
        result = r / 0.5
        self.assertEqual(result, Rational(1, 1))

    def test_float_to_rational(self):
        r = Rational.float_to_rational(0.75)
        self.assertEqual(r, Rational(7500000000, 10000000000))

    def test_float_to_rational_rounding(self):
        r = Rational.float_to_rational(1/3)
        self.assertEqual(r, Rational(3333333333, 10000000000))

    def test_pow_float(self):
        r = Rational(9, 4)
        result = r ** 0.5
        self.assertEqual(result, Rational(3, 2))

    def test_pow_negative_float(self):
        r = Rational(9, 4)
        result = r ** -0.5
        self.assertEqual(result, Rational(2, 3))

    def test_iadd_int(self):
        r = Rational(1, 2)
        r += 3
        self.assertEqual(r, Rational(7, 2))

    def test_imul_int(self):
        r = Rational(1, 2)
        r *= 3
        self.assertEqual(r, Rational(3, 2))

    def test_itruediv_int(self):
        r = Rational(3, 4)
        r /= 2
        self.assertEqual(r, Rational(3, 8))

    def test_eq_int(self):
        r = Rational(5, 1)
        self.assertTrue(r == 5)

    def test_eq_int_false(self):
        r = Rational(5, 2)
        self.assertFalse(r == 5)

    def test_neq_int(self):
        r = Rational(5, 2)
        self.assertTrue(r != 5)

    def test_neq_int_false(self):
        r = Rational(5, 1)
        self.assertFalse(r != 5)

    def test_truediv_type_error(self):
        r = Rational(1, 2)
        with self.assertRaises(TypeError):
            _ = r / "test"

    def test_root(self):
        r = Rational(8, 27)
        result = Rational.root(r, 3)
        self.assertEqual(result, Rational(2, 3))

    def test_root_irrational(self):
        r = Rational(2, 3)
        with self.assertRaises(ValueError):
            Rational.root(r, 2)

    def test_str_whole_number(self):
        r = Rational(5, 1)
        self.assertEqual(str(r), "5")

    def test_str_fraction(self):
        r = Rational(3, 4)
        self.assertEqual(str(r), "3/4")

    def test_str_negative_numerator(self):
        r = Rational(-2, 3)
        self.assertEqual(str(r), "-2/3")


if __name__ == '__main__':
    unittest.main()