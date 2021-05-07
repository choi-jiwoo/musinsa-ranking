from bs4 import BeautifulSoup as bs
import re
import requests
import pandas as pd

def get_ranking(url):
    """
    :param url: website url to scrape
    :return: DataFrame
    """
    res = requests.get(url)
    soup = bs(res.text, "html.parser") 
    ranking_section = soup.find(class_ = 'tbl_box_sranking')

    # keyword
    item_html = ranking_section.find_all('a')
    # rank change direction
    status_html = ranking_section.find_all(class_='arrow')
    # rank changes
    chng_html = ranking_section.find_all(class_='p_srank_last')

    item = []
    status = []
    change = []

    for i in range(len(status_html)):
        item.append(item_html[i].attrs['title'])
        status.append(status_html[i].get_text())
        change.append(re.sub(r'[^0-9]','',chng_html[i].get_text()))

    # save data in dataframe
    df = pd.DataFrame(list(zip(item, status, change)), columns=['Item','Status','Change'],
                      index=list(range(1,len(status_html)+1)))

    return df