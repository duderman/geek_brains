import unittest
from fabric import Cloth, Coat, Suit


class TestCloth(unittest.TestCase):
  def test_fabric_total(self):
    coat1 = Coat(65)
    coat2 = Coat(650)
    suit2 = Suit(10)
    suit1 = Suit(20)

    clothes = [coat1, coat2, suit1, suit2]

    self.assertEqual(Cloth.fabric_total(clothes), 10.5 + 100.5 + 20.3 + 40.3)


class TestCoat(unittest.TestCase):
  def test_size_getter(self):
    coat = Coat(1)
    self.assertEqual(coat.size, 1)

  def test_fabric_amount(self):
    coat = Coat(65)
    self.assertEqual(coat.fabric_amount(), 10.5)


class TestSuit(unittest.TestCase):
  def test_height_getter(self):
    suit = Suit(1)
    self.assertEqual(suit.height, 1)

  def test_fabric_amount(self):
    suit = Suit(10)
    self.assertEqual(suit.fabric_amount(), 20.3)


if __name__ == '__main__':
    unittest.main()
