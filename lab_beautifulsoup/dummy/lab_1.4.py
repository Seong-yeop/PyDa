import requests
import csv
from bs4 import BeautifulSoup

def get_prof_url(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    #last_links = soup.find(class_='AlphaNav')
    #last_links.decompose()

    f = csv.writer(open('prof_url.csv', 'w'))
    f.writerow(['Name', 'Link'])

    body = soup.find(class_='section clearfix2')
    prof_name_list = body.find_all('span',class_='field-content')
    prof_name_list_link = [v.find('a').get('href') for v in prof_name_list]
    prof_name = [v.find('a').get_text() for v in prof_name_list]
    for name,link in zip(prof_name, prof_name_list_link):
        names = name
        links = 'https://cse.snu.ac.kr/' + link
        f.writerow([names, links])
        
  
if __name__=='__main__':
    url = 'https://cse.snu.ac.kr/people/faculty'
    get_prof_url(url)