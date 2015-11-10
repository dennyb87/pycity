import unittest
from int_format import format

class IntFormatTest(unittest.TestCase):
    
    def test_format(self):
        self.assertEqual(format("1", 2), "01")

if __name__ == "__main__":
    unittest.main()
