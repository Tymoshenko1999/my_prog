import requests
from time import sleep
import html5lib
from bs4 import BeautifulSoup
from selenium import webdriver

headers = {   # для GET
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

headers1 = {   # для POST
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'X-CSRF-TOKEN':'',
    'X-Requested-With': 'XMLHttpRequest'
}

headers2 = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'X-CSRF-TOKEN':'',
    'X-Requested-With': 'XMLHttpRequest',
    'Set-Cookie':''
    }

login_data = {
    'uid': 'username',
    'password': 'password'
}

with requests.Session() as s:
    url = 'https://polynet.lviv.ua/login'
    url2 = 'https://polynet.lviv.ua/port/on'
    r = s.get(url, headers=headers)
    print (r.content)
    #sleep(5)
    soup = BeautifulSoup(r.content, 'html5lib')
    #sleep(5)
    headers1['X-CSRF-TOKEN'] = soup.find('meta', attrs={'name': 'csrf-token'})['content']
    print(headers1['X-CSRF-TOKEN'])
    r = s.post(url, data=login_data, headers=headers1)
    headers2['X-CSRF-TOKEN'] = soup.find('meta', attrs={'name': 'csrf-token'})['content']
    headers2['Set-Cookie'] = str(s.cookies.get_dict())
    r = s.post(url2, data=login_data, headers=headers2)
    f = open('polynet.txt', 'w')
    f.write(str(r.text))  
    f.close()
    print(r.text)
    print (s.cookies)
    print(s.cookies.get_dict())
