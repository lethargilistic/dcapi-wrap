import requests
from urllib.parse import urlparse
from os.path import join

#TODO: Break into separate standard settings module
ROOT_URL = 'http://progdisc.club/~lethargilistic/proxy'
HEADERS = {'User-Agent': 'dcapi-wrap (https://github.com/lethargilistic/dcapi-wrap)'}

def set_url(url):
    if urlparse(url):
        ROOT_URL = url
    else:
        raise ValueError('The URL was not a URL')

def character(search):
    search_url = join(ROOT_URL, 'character', str(search))
    response = requests.get(search_url, headers=HEADERS)
    if response.status_code != 200:
        raise ConnectionError('API endpoint returned status '
                                + str(response.status_code))

    return response.json()

if __name__ == '__main__':
    print(character(0))
    print(character('Ai Haibara'))
