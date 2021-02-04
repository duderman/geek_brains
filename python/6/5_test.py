import unittest
m = __import__('5')


class TestStationery(unittest.TestCase):
  def test_draw(self):
    """
    Tests that stationery returns a correct message
    """
    Stationery = m.Stationery('yo')

    self.assertEqual(Stationery.draw(), 'Starting to draw')


class TestPen(unittest.TestCase):
  def test_draw(self):
    """
    Tests that pen returns a correct message
    """
    pen = m.Pen('yo')

    self.assertEqual(pen.draw(), 'Drawing with a pen')


class TestPencil(unittest.TestCase):
  def test_draw(self):
    """
    Tests that pencil returns a correct message
    """
    pencil = m.Pencil('yo')

    self.assertEqual(pencil.draw(), 'Drawing with a pencil')


class TestHandle(unittest.TestCase):
  def test_draw(self):
    """
    Tests that handle returns a correct message
    """
    handle = m.Handle('yo')

    self.assertEqual(handle.draw(), 'Drawing with a handle')


if __name__ == '__main__':
    unittest.main()
