import requests
import html

from bs4 import BeautifulSoup


def show_news(NB_receive):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683'}

    data = requests.get('https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q=' + NB_receive + ' 부동산', headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')
    news = soup.select('#mArticle>.inner_article>.g_comp>#newsColl>.coll_cont')


    news_list = {}
    n_list = []


    for new in news:
        link = new.select_one('#clusterResultUL > li')
        if not link == None:
            news_list['news_show'] = [link]
            html_news = news_list['news_show']
            html_data1 = list(html_news[0])
            print(html_data1[1])




            # n_list.append({'title': html_data2, 'href': html_data1})

https://search.pstatic.net/common/?src=https%3A%2F%2Fimgnews.pstatic.net%2Fimage%2Forigin%2F5055%2F2016%2F01%2F20%2F245341.jpg&type=ofullfill80_80_q75_re2
https://search.pstatic.net/common/?src=https%3A%2F%2Fimgnews.pstatic.net%2Fimage%2Forigin%2F5338%2F2019%2F06%2F25%2F46159.jpg&type=ofullfill80_80_q75_re2


show_news('신갈동')