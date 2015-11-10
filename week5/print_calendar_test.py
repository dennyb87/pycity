import unittest
from print_calendar import (
    getMonthName,
    getStartDay,
    getTotalNumberOfDays,
    getNumberOfDaysInMonth,
    isLeapYear,
)

class PrintCalendarTest(unittest.TestCase):

    def test_getMonthName(self):
        self.assertEqual(getMonthName(1), "January")

    def test_getStartDay(self):
        self.assertEqual(getStartDay(2000, 1), 6)

    def test_getTotalNumberOfDays(self):
        self.assertEqual(getTotalNumberOfDays(2000, 1), 73048)

    def test_getNumberOfDaysInMonth(self):
        self.assertEqual(getNumberOfDaysInMonth(2000, 2), 29)

    def test_isLeapYear(self):
        self.assertEqual(isLeapYear(2000), True)

if __name__ == "__main__":
    unittest.main()
