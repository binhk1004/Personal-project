import requests
import html

from bs4 import BeautifulSoup


def show_news(NB_receive):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683'}

    data = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=' + NB_receive + ' 부동산', headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')
    # news = soup.select('#container > #main_pack > .news mynews section _prs_nws > .type01' )
    news = soup.select('#main_pack > .news > .type01 > li')

    for new in news:
        link = new.select_one('dl > dt > a')
        if not link == None:
            print(link)
    # print(news)

show_news('신갈동')