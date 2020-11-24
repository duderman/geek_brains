# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import click


@click.command()
@click.option('-b', '--bonus', default=0, help='Employee bonus')
@click.argument('hours', required=True, type=int)
@click.argument('rate', required=True, type=int)
def cli(hours, rate, bonus):
  """Calculate employee income

  Income is calculated using formula: (HOURS * RATE) + bonus
  """
  income = hours * rate + bonus
  click.echo(f"Employee income: {income}")


if __name__ == '__main__':
  cli()
