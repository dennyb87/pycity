import unittest
from matrix import squareMatrix

class MatrixTest(unittest.TestCase):
    
    def test_squareMatrix(self):
        matrix = squareMatrix(2)
        self.assertEqual(matrix.__class__, list)
        self.assertEqual(len(matrix), 2)

if __name__ == "__main__":

    unittest.main()
