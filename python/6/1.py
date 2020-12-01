# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
#
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep


class TrafficLight():
  """
  Implements traffic light switch
  """

  COLORS_WITH_DURATION = {
      'red': 7,
      'yellow': 2,
      'green': 7
  }

  def __init__(self):
    self.__current_index = 0

  def run(self):
    while self.__current_color():
      self.__log_color()
      self.__wait()
      self.__next()

  def __log_color(self):
    print(
        f"Current color is {self.__current_color()}. It'll be on for {self.__current_secs()} secs")

  def __wait(self):
    sleep(self.__current_secs())

  def __next(self):
    self.__current_index += 1

  def __current_secs(self):
    return self.COLORS_WITH_DURATION[self.__current_color()]

  def __current_color(self):
    if self.__current_index == len(self.COLORS_WITH_DURATION):
      return

    return list(self.COLORS_WITH_DURATION)[self.__current_index]


traffic_light = TrafficLight()
traffic_light.run()
