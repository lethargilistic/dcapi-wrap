import requests
from os.path import join

DEFAULT_URL = 'progdisc.club/~lethargilistic/proxy'

class Dcapi():
    def __init__(self, url=None):
        self.url = 'http://'
        if url:
            self.url += url
        else:
            self.url += DEFAULT_URL
        self.headers = {'User-Agent': 'dcapi-wrap'} 

    def character(self, search):
        search_url = join(self.url, 'character', str(search))
        return requests.get(search_url, headers=self.headers).json()


if __name__ == '__main__':
    api = Dcapi('127.0.0.1:8000')
    print(api.character(1))
    print(api.character('Ai Haibara'))
