import unittest
m = __import__('4')


class TestCar(unittest.TestCase):
  def build_car(self, klass=m.Car, speed=4):
    return klass(speed, 'red', 'my car')

  def test_attributes(self):
      """
      Test that attributes are properly set
      """
      car = self.build_car()

      self.assertEqual(car.speed, 4)
      self.assertEqual(car.color, 'red')
      self.assertEqual(car.name, 'my car')

  def test_is_police(self):
    """
    Test that Car isn't initialzed as a police car
    """
    car = self.build_car()
    self.assertEqual(car.is_police, False)

  def test_go(self):
    """
    Test go method
    """
    car = self.build_car()
    self.assertEqual(car.go(), 'Wroom wroom')

  def test_stop(self):
    """
    Test stop method
    """
    car = self.build_car()
    self.assertEqual(car.stop(), 'SCREEEEEECH!')

  def test_turn(self):
    """
    Test successful turn method
    """
    car = self.build_car()
    self.assertEqual(car.turn('left'), 'Turning left')
    self.assertEqual(car.turn('right'), 'Turning right')
    self.assertEqual(car.turn('back'), 'Turning back')

  def test_failing_turn(self):
    """
    Test that #turn is failing if called with unknown direction
    """
    car = self.build_car()
    with self.assertRaises(m.UnkonwnDirection) as context:
      car.turn('unknown')
      self.assertTrue("Unknown direction 'unkown'" in context.exception)

  def test_show_speed(self):
    """
    Test simple show_speed case
    """
    car = self.build_car()
    self.assertEqual(car.show_speed(), 4)


class TestTownCar(TestCar):
  def build_car(self, speed=4):
    return super().build_car(m.TownCar, speed)

  def test_speed_limit(self):
    """
    Test TownCar speed limit
    """
    car = self.build_car(61)

    with self.assertRaises(m.TooFast) as context:
      car.show_speed()
      self.assertTrue(
          'The car is going too fast. Max speed for this vehicle is 60 km/h' in context.exception)


class TestWorkCar(TestCar):
  def build_car(self, speed=4):
    return super().build_car(m.WorkCar, speed)

  def test_speed_limit(self):
    """
    Test WorkCar speed limit
    """
    car = self.build_car(41)

    with self.assertRaises(m.TooFast) as context:
      car.show_speed()
      self.assertTrue(
          'The car is going too fast. Max speed for this vehicle is 40 km/h' in context.exception)


class TestPoliceCar(TestCar):
  def build_car(self):
    return super().build_car(m.PoliceCar)

  def test_is_police(self):
    """
    Test that PoliceCar is actualy a police car
    """
    car = self.build_car()
    self.assertEqual(car.is_police, True)


if __name__ == '__main__':
    unittest.main()
