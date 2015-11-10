import unittest
from card_validation import (
    numberToMatrix,
    getOddDigits,
    getEvenDigits,
    sumOfDoubleOddPlace,
    sumOfEvenPlace,
    getDigit,
    isValid
)

class CardValidationTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        self.card_number = "4388576018410707"
        self.matrix = numberToMatrix(self.card_number)
        self.odds = getOddDigits(self.matrix)
        self.evens = getEvenDigits(self.matrix)
    
    def test_numberToMatrix(self):
        self.assertEqual(self.matrix.__class__, list)

    def test_getOddDigits(self):
        self.assertEqual(self.odds.__class__, list)

    def test_getEvenDigits(self):
        self.assertEqual(self.evens.__class__, list)

    def test_sumOfDoubleOddPlace(self):
        self.assertEqual(sumOfDoubleOddPlace(self.odds), 29)

    def test_getDigit(self):
        self.assertEqual(getDigit(9), 9)

    def test_isValid(self):
        self.assertEqual(isValid(self.card_number), True)

if __name__ == "__main__":

    unittest.main()
