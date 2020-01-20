from bs4 import BeautifulSoup
import requests
import pandas as pd


def get_rank(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    item_box = soup.find_all('div', class_='rank_inner v2')

    title = [item.find('span', class_='title_cell').get_text().strip()
             for item in item_box]
    item_list = [{head.get_text().strip(): value.get_text().strip() for head, value in zip(
        item.find_all('em', class_='num'), item.find_all('span', class_='title'))} for item in item_box]
    rank = [list(v) for v in zip(title, item_list)]
    return rank


if __name__ == '__main__':
    url = 'https://datalab.naver.com/'
    rank = get_rank(url)
    print(rank)
