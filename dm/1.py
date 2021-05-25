from requests import get
from json import dump

PUBLIC_APIS_URL = 'https://api.publicapis.org/entries'


def to_snake_case(value):
    return value.lower().replace(' ', '_')


categories = {}


def add_api(api):
    category = api.pop("Category")
    categories.setdefault(category, [])
    categories[category].append(api)


def write_category_to_file(category, apis):
    snaked_category = to_snake_case(category)
    file_name = snaked_category + '.json'
    print(f"Writing category '{category}' with {len(apis)} APIs to file '{file_name}'")
    data = {'category': category, 'apis': apis}
    with open(file_name, 'w') as out_file:
        dump(data, out_file)


request = get(PUBLIC_APIS_URL)

if request.status_code != 200:
    print(f"Request returned HTTP status {request.status_code}")
    exit(1)

for api in request.json()['entries']:
    add_api(api)

print(f"{request.json()['count']} API in {len(categories)} categories found")

for category, apis in categories.items():
    write_category_to_file(category, apis)

print('DONE!')

exit(0)
