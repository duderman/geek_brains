import csv
import json

successful_companies = {}
profits = []

with open('companies.tsv') as tsvfile:
  reader = csv.DictReader(tsvfile, delimiter="\t")
  for row in reader:
    profit = int(row['income']) - int(row['expences'])
    profits.append(profit)

    if profit < 1:
      continue

    successful_companies[row['name']] = profit

average_profit = round(sum(profits) / len(profits))
averages = {'average_profit':  average_profit}
result = [successful_companies, averages]
result_content = json.dumps(result)

with open('companies_success.json', 'w') as file:
  file.write(result_content)
