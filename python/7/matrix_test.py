import unittest
from matrix import Matrix, WrongSize


class TestMatrix(unittest.TestCase):
  def test_str(self):
    """
    Tests Matrix stringifying
    """
    matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [9, 8, 7]])
    self.assertEqual(str(matrix), "⌈ 1 2 3 ⌉\n| 4 5 6 |\n⌊ 9 8 7 ⌋")

  def test_str_when_empty(self):
    """
    Test str of empty matrix
    """
    matrix = Matrix([])
    self.assertEqual(str(matrix), '')

  def test_wrong_size(self):
    """
    Init fails when matrix has wrong sizes
    """
    self.assertRaises(WrongSize, Matrix, [[1], [2, 3]])


if __name__ == '__main__':
    unittest.main()
