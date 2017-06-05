import requests
from urllib.parse import urlparse
from os.path import join

#TODO: Break into separate standard settings module
ROOT_URL = 'http://progdisc.club/~lethargilistic/proxy'
HEADERS = {'User-Agent': 'dcapi-wrap'}#TODO: include github link 

def set_url(url):
    if urlparse(url):
        ROOT_URL = url
    else:
        raise ValueError('The URL was not a URL')

def character(search):
    search_url = join(ROOT_URL, 'character', str(search))
    json_dict = requests.get(search_url, headers=HEADERS).json()
    return json_dict

if __name__ == '__main__':
    #set_url('127.0.0.1:8000')
    print(character(0))
    print(character('Ai Haibara'))
