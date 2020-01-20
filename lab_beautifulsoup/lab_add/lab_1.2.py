### 다음 뉴스 웹 크롤링 하기 ###

import requests
from bs4 import BeautifulSoup

page = requests.get("https://media.daum.net/digital/")
soup = BeautifulSoup(page.content, 'html.parser')

class_ = ['section_cate section_issue', 'section_cate section_headline', 'section_cate section_ranking','box_timenews' ,'aside_g aside_ranking']
'''
for _class in class_:
    title_section = soup.find('div',{'class':_class})
    link_title = title_section.find_all('a', {'class':'link_txt'})
    for num in range(len(link_title)):
        print(link_title[num].get_text().strip())
'''

title_section = soup.find_all('div',{'class': class_})

for section in title_section:
    link_title = section.find_all('a',{'class':'link_txt'})
    for num in range(len(link_title)):
        print(link_title[num].get_text().strip())

