import unittest
from primer import isPrime, primeInRange

class PrimerTest(unittest.TestCase):
    
    def test_isPrime(self):
        self.assertEqual(isPrime(2), True)

    def test_primeInRange(self):
        self.assertEqual(primeInRange(2,10), [2, 3, 5, 7])


if __name__ == "__main__":

    unittest.main()
