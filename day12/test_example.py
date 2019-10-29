from unittest import TestCase

from example import super_sum


class TestExample(TestCase):
    def test_sum_one_plus_two_eq_three(self):
        # given
        a = 1
        b = 2
        expected = 3
        result = super_sum(a, b)
        self.assertEqual(result, expected)

    def test_sum_raises_value_err_for_int_and_str(self):
        # given
        a = 'abc'
        b = 3
        with self.assertRaises(TypeError):
            super_sum(a, b)

    def test_sum_adds_3_numers(self):
        # given
        data = [1, 2, 3]
        expected = 6
        result = super_sum(*data)
        self.assertEqual(result, expected)