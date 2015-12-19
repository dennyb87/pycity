#!/usr/bin/env python3
import unittest
from body_mass import bmi_calculator


class BodyMassTest(unittest.TestCase):

    def setUp(self):
        self.bmi1 = bmi_calculator(45, 1.65)
        self.bmi2 = bmi_calculator(65, 1.65)
        self.bmi3 = bmi_calculator(75, 1.65)
        self.bmi4 = bmi_calculator(85, 1.65)

    def test_bmi_calculator(self):
        self.assertEqual(self.bmi1, 'Underweight')
        self.assertEqual(self.bmi2, 'Normal')
        self.assertEqual(self.bmi3, 'Overweight')
        self.assertEqual(self.bmi4, 'Obese')


if __name__ == "__main__":
    unittest.main()
