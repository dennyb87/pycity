import unittest
from days_in_a_year import (
    isLeapYear, numberOfDaysInAYear, numberOfDaysInRange
)

class DaysInAYearTest(unittest.TestCase):
    
    def test_isLeapYear(self):
        self.assertEqual(isLeapYear(2000), True)
        self.assertEqual(isLeapYear(2001), False)

    def test_numberOfDaysInAYear(self):
        self.assertEqual(numberOfDaysInAYear(2000), 366)
        self.assertEqual(numberOfDaysInAYear(2001), 365)

    def test_numberOfDaysInRange(self):
        self.assertEqual(numberOfDaysInRange(2000, 2001), 366)

if __name__ == "__main__":

    unittest.main()
