# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class UnkonwnDirection(Exception):
  pass


class TooFast(Exception):
  pass


class Car():
  """
  Base car
  """

  DIRECTIONS = ['back', 'left', 'right']

  def __init__(self, speed, color, name, is_police=False, max_speed=None):
    self.speed = speed
    self.color = color
    self.name = name
    self.is_police = is_police
    self.__max_speed = max_speed

  def go(self):
    """
    Starts the car

    Returns:
        string: Car moving sound
    """
    return 'Wroom wroom'

  def stop(self):
    """
    Stops the car

    Returns:
        string: Brakes sound
    """
    return 'SCREEEEEECH!'

  def turn(self, direction):
    """
    Turns the car

    Args:
        direction (string): One of the directions (left, right, back)

    Raises:
        UnkonwnDirection: If passed an unknown direction

    Returns:
        string: Turn message
    """
    if direction not in self.DIRECTIONS:
      raise UnkonwnDirection(f"Unknown direction '{direction}'")

    return f"Turning {direction}"

  def show_speed(self):
    """
    Show current speed of the car

    Returns:
        int: Current speed
    """
    if self.__max_speed and self.speed > self.__max_speed:
      raise TooFast('The car is going too fast. ' +
                    f"Max speed for this vehicle is {self.__max_speed} km/h")
    return self.speed


class TownCar(Car):
  """
  Town Car
  """

  def __init__(self, speed, color, name):
    super().__init__(speed, color, name, max_speed=60)


class SportCar(Car):
  """
  Sport Car
  """


class WorkCar(Car):
  """
  Work Car
  """

  def __init__(self, speed, color, name):
    super().__init__(speed, color, name, max_speed=40)


class PoliceCar(Car):
  """
  Police Car
  """

  def __init__(self, speed, color, name):
    super().__init__(speed, color, name, is_police=True)
