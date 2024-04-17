import requests


def get_search(name):
    url = f'https://openlibrary.org/search.json?q={name}&fields=title,author_name,first_publish_year'
    data = requests.get(url).json()
    return data


result = get_search('dune')
print(result)



