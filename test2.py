import requests
import html

from bs4 import BeautifulSoup

def show_news(NB_receive):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683'}

    data = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=' + NB_receive + ' 부동산',
                        headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')
    news = soup.select('#main_pack > .news > .type01 > li')

    news_list = {}
    n_list = []

    for new in news:
        link = new.select_one('dl > dt > a')
        if not link == None:
            news_list['news_show'] = [link]
            html_news = news_list['news_show']

            html_data1 = html_news[0]['href']

            html_data2 = html_news[0]['title']
            for img in news:
                image = new.select_one('.thumb > a > img')
                if not image == None:
                    news_list['news_img'] = [image]
                    html_image = news_list['news_img']
                    html_img = html_image[0]['src']
                    print(html_img)

    #         n_list.append({'title': html_data2, 'href': html_data1, 'image':html_img})
    # print(n_list)



show_news('신갈동')