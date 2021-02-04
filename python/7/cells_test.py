import unittest
from cells import Cell, SecondCellTooBig, ZeroAmount


class TestCell(unittest.TestCase):
  def test_add(self):
    cell1 = Cell(1)
    cell2 = Cell(2)
    cell3 = cell1 + cell2

    self.assertEqual(cell3.amount, 3)
    self.assertNotEqual(cell3, cell1)
    self.assertNotEqual(cell3, cell2)

  def test_sub(self):
    cell1 = Cell(3)
    cell2 = Cell(1)
    cell3 = cell1 - cell2

    self.assertEqual(cell3.amount, 2)
    self.assertNotEqual(cell3, cell1)
    self.assertNotEqual(cell3, cell2)

  def test_sub_fail(self):
    def f(): return Cell(1) - Cell(2)
    self.assertRaises(SecondCellTooBig, f)

  def test_mul(self):
    cell1 = Cell(2)
    cell2 = Cell(2)
    cell3 = cell1 * cell2

    self.assertEqual(cell3.amount, 4)
    self.assertNotEqual(cell3, cell1)
    self.assertNotEqual(cell3, cell2)

  def test_div(self):
    cell1 = Cell(4)
    cell2 = Cell(2)
    cell3 = cell1 / cell2

    self.assertEqual(cell3.amount, 2)
    self.assertNotEqual(cell3, cell1)
    self.assertNotEqual(cell3, cell2)

  def test_div_round(self):
    cell = Cell(3) / Cell(2)
    self.assertEqual(cell.amount, 1)

  def test_div_by_zero(self):
    def f(): return Cell(1) / Cell(0)
    self.assertRaises(ZeroAmount, f)

  def test_make_order(self):
    cell = Cell(3)
    self.assertEqual(cell.make_order(5), '***..')
    self.assertEqual(cell.make_order(3), '***')
    self.assertEqual(cell.make_order(2), "**\n*.")

  def test_div_by_zero(self):
    cell = Cell(1)
    self.assertRaises(ZeroAmount, cell.make_order, 0)


if __name__ == '__main__':
    unittest.main()
