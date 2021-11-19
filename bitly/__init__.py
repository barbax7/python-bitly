import requests

__version__ = '1.0.1'

class Bitly():
    "Connect to Bitly with Access Token"

    def __init__(self, token: str):
        if token is None or token == '': raise BitlyException(000, 'Empty token! Please give a valid token')
        self.TOKEN = token
        
        self.headers = {
            'Authorization': 'Bearer {}'.format(self.TOKEN),
            'Content-Type': 'application/json'
        }

    def shorten(self, long_url: str):
        "Shorten the given link"

        headers = self.headers

        data = '{"long_url": "%s", "domain": "bit.ly"}' % long_url

        response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers = headers, data = data)
        if response.status_code == 200 or response.status_code == 201 : return response.json()['link']
        elif response.status_code == 403: raise BitlyException(403, 'Your acccess token is invalid, please give valid one.')
        else: raise BitlyException(response.status_code, response.json()['description'])
    
    def expand(self, short_url: str):
        "Obtain the long url from a short link"

        headers = self.headers

        if "http://" in short_url:
            short_url = short_url.replace("http://","")
        if "https://" in short_url:
            short_url = short_url.replace("https://","")

        data = '{ "bitlink_id": "%s" }' % short_url

        response = requests.post('https://api-ssl.bitly.com/v4/expand', headers=headers, data=data)

        if response.status_code == 200 or response.status_code == 201 : return response.json()['long_url']
        elif response.status_code == 403: raise BitlyException(403, 'Your acccess token is invalid, please give valid one.')
        else: raise BitlyException(response.status_code, response.json()['description'])
            
class Connection(Bitly):
    pass

class BitlyException(Exception):
    def __init__(self, status_code, description):
        pass
