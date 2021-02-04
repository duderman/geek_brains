import unittest

from warehouse import Warehouse, Unit, NoUnitsLeft


class Test(unittest.TestCase):
  def test_add(self):
    warehouse = Warehouse()
    unit = Unit('company', 'model1')
    warehouse.add_unit(unit)
    self.assertEqual(warehouse.units[Unit], [unit])

  def test_give_unit_of_type(self):
    warehouse = Warehouse()
    unit = Unit('company', 'model1')
    warehouse.add_unit(unit)
    given_unit = warehouse.give_unit_of_type(Unit)
    self.assertEqual(unit, given_unit)
    self.assertRaises(NoUnitsLeft, warehouse.give_unit_of_type, Unit)


if __name__ == '__main__':
    unittest.main()
