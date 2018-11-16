""" Tests our prime number function """

import unittest
from primeNumbers import generate_prime_nums

class TestPrimeNumbers(unittest.TestCase):
    """ Tests prime_numbers functionality """

    def test_input_is_positive(self):
        self.assertEqual(generate_prime_nums(-5), [])
    def test_input_is_Not_a_list(self):
    	self.assertRaises(TypeError,generate_prime_nums, [2,4])
    def test_input_is_zero(self):
        self.assertEqual(generate_prime_nums(0), [])
    def test_output_is_primeNumbers(self):
        self.assertEqual(generate_prime_nums(8), [2,3,5,7])
    def test_input_is_not_a_dictionary(self):
        self.assertRaises(TypeError,generate_prime_nums, {"jane":2, "tom":4})
if __name__ == "__main__":
    unittest.main(exit = False)
