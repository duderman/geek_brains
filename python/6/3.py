# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}.
#
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker():
  """
  Company employee info
  """

  def __init__(self, first_name, last_name, position, wage, bonus):
    self.first_name = first_name
    self.last_name = last_name
    self.position = position
    self.__income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
  """
  Employee info accessor
  """

  def __init__(self, first_name, last_name, position, wage, bonus):
    super().__init__(first_name, last_name, position, wage, bonus)

  def get_full_name(self):
    return f"{self.first_name} {self.last_name}"

  def get_total_income(self):
    return self._Worker__income['wage'] + self._Worker__income['bonus']


position = Position('Kolka', 'Bog', 'Dev', 80000, 5000)
print(position.get_full_name())
print(position.get_total_income())
