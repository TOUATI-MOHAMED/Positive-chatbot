#Building a chatbot with Deep NLP
from bs4 import BeautifulSoup as bs
import requests as rq
import pandas as pd
import time

urls = pd.read_csv("test.csv")

urls_list = []

scrap = []

for url in urls.itertuples():
    if 'verywellmind' in url.URL :
        ch = url.URL.strip("'")
        urls_list.append(ch)
        
for url in urls_list :
    if url is None : 
        continue
    page = rq.get(url)
    #print(page.status_code)
    #parsing the page
    soup = bs(page.content, 'html.parser')
    paragraphs = []
    page_content = soup.find('div', class_ = 'comp structured-content article-content expert-content right-rail__offset lock-journey mntl-sc-page mntl-block')
    if page_content is None :
        continue
    
    for e in page_content.find_all("p"):
        if None in (e):
            continue
        paragraphs.append(e.get_text())

    for e in page_content.find_all("li"):
        if None in (e):
            continue
        paragraphs.append(e.get_text())
        
    scrap.append(' '.join(paragraphs))
    time.sleep(3)
    
df = pd.DataFrame(scrap)
df.to_csv('scrap.csv', index = False)
print (df)


#use a string instead of paragraphs list and concatenate with .join(list)


