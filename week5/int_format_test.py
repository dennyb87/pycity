import unittest


class Test(unittest.TestCase):
    
    def test_format(self):
        self.assertEqual(format("1", 2), "01")

if __name__ == "__main__":

    from int_format import format
    unittest.main()
