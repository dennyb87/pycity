import unittest


class Test(unittest.TestCase):
    
    def test_footToMeters(self):
        self.assertEqual(footToMeter(1), 0.305)

    def test_meterToFoot(self):
        self.assertEqual(meterToFoot(0.305), 1)


if __name__ == "__main__":

    from feet_meters import footToMeter, meterToFoot
    unittest.main()
