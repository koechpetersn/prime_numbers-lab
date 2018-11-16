""" Tests our prime number function """

import unittest
from classprime import PrimeNumber

class TestPrimeNumbers(unittest.TestCase):
    """ Tests prime_numbers functionality """

    def test_input_is_positive(self):
      num = PrimeNumber()
      self.assertEqual(num.generate_prime(-5), [])

    def test_input_is_Not_a_list(self):
      num = PrimeNumber()
      self.assertRaises(TypeError,num.generate_prime, [2,4])

    def test_input_is_zero(self):
      num = PrimeNumber()
      self.assertEqual(num.generate_prime(0), [])

    def test_output_is_primeNumbers(self):
      num = PrimeNumber()
      self.assertEqual(num.generate_prime(8), [2,3,5,7])
    def test_input_is_not_a_dictionary(self):
      num = PrimeNumber()
      self.assertRaises(TypeError,num.generate_prime, {"jane":2, "tom":4})

if __name__ == "__main__":
    unittest.main(exit = False)
