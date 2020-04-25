import requests
import html

from bs4 import BeautifulSoup


def show_news(NB_receive):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683'}

    data = requests.get('https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q=' + NB_receive + ' 부동산', headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')
    news = soup.select('.inner_article>.g_comp>#newsColl>.coll_cont')

    news_list = {}
    n_list = []


    for new in news:
        link = new.select_one('#clusterResultUL > li')
        if not link == None:
            news_list['news_show'] = [link]
            print(news_list)
        #     html_news = news_list['news_show']
        #
        #     html_data1 = html_news[0]['href']
        #     html_data2 = html_news[0]['title']
        #
        #     n_list.append({'title': html_data2, 'href': html_data1})
        # print(n_list)



show_news('신갈동')