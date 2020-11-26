import csv

loosers = []
salaries = []

with open('employees.csv') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    salary = int(row['salary'])
    salaries.append(salary)
    if salary > 20000:
      continue
    loosers.append(row['last_name'])

if len(loosers) == 0:
  print('Everyone is doing great!')
else:
  loosers_s = ', '.join(loosers)
  print(f"Look at theese loosers: {loosers_s}")

median = round(sum(salaries) / len(salaries))
print(f"Average income is {median}")
