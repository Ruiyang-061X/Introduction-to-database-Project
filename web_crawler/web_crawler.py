import random
import time
import requests
from bs4 import BeautifulSoup

from short_film_comment_app.models import Film


headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

for i in range(0, 250, 25):
    url = 'https://movie.douban.com/top250?start={}&filter='.format(i)
    html = requests.get(url, headers=headers).content
    soup = BeautifulSoup(html, 'lxml')
    for j in soup.find(id='wrapper').find_all('li'):
        id = j.em.get_text()
        image_path = 'short_film_comment_app/images/poster/{}.jpg'.format(id)
        image = requests.get(j.img['src']).content
        file = open('image/{}.jpg'.format(id), 'wb')
        file.write(image)
        file.close()
        caption = j.span.get_text()
        information = j.find_all('p')[0].get_text()
        information2 = ''
        if(len(j.find_all('p')) > 1):
            information2 = j.find_all('p')[1].get_text()
        html = requests.get(j.a['href'], headers=headers).content
        soup = BeautifulSoup(html, 'lxml')
        if(len(soup.find(id='link-report').find_all('span')) > 2):
            introduction = soup.find(id='link-report').find_all('span')[2].get_text()
        else:
            introduction = soup.find(id='link-report').find_all('span')[0].get_text()
        a = Film(id=id, image_path=image_path, caption=caption, information=information, information2=information2, introduction=introduction)
        a.save()
        print(id)
        print(image_path)
        print(caption)
        print(information)
        print(information2)
        print(introduction)
        time.sleep(random.uniform(0.5, 1))