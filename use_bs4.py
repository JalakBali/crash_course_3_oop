import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'
try:
    respons = requests.get(url)
    if respons.status_code == 200:
            print(f'sukses, respons = {respons.status_code}')
            #print(f'content {respons.text}')
            soup = BeautifulSoup(respons.text, features="html.parser")
            print(f'hasil pemanggilan {url}')
            print(f'titel: {soup.title.string}')
    else:
        print(f'woops ada kesalahan request {respons.status_code}')
except Exception as e :
    print('there is an error',e)
print('program ended')
