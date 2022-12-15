import requests, json

api_key = "390a41eae3fd4ea89c9153640221412"

class book:
    def __init__(self, link, image, title):
        self.link  = link
        self.image = image 
        self.title = title

def get_description(city):
    base_url = " http://api.weatherapi.com/v1/current.json"

    complete_url = base_url + "?key=" + api_key + "&q="+city

    print(complete_url)
    response = requests.get(complete_url)

    x = response.json()
    return x['current']['condition']['text']

    """
    if "error" not in x:
        return x['data'][0]['weather']['description']
    else:
        print("City Not Found ")
    """

def get_books_season(season):
    url = 'https://www.googleapis.com/books/v1/volumes?q='+season
    resp = requests.get(url)
    json = resp.json()

    titles = []

    for i in json['items']:
        if 'categories' in i['volumeInfo'] and 'Computers' not in i['volumeInfo']['categories']:
            titles.append(book(i['volumeInfo']['previewLink'], i['volumeInfo']['imageLinks']['thumbnail'], i['volumeInfo']['title']).__dict__)
    return titles


def get_books(city):
    description = get_description(city)
    print(description)
    desc_list = description.split(' ')
    desc_list_join = '+'.join(desc_list)

    url = 'https://www.googleapis.com/books/v1/volumes?q='+description
    resp = requests.get(url)
    json = resp.json()

    titles = []

    for i in json['items']:
        if 'categories' in i['volumeInfo'] and 'Computers' not in i['volumeInfo']['categories']:
            titles.append(book(i['volumeInfo']['previewLink'], i['volumeInfo']['imageLinks']['thumbnail'], i['volumeInfo']['title']).__dict__)
    return titles
