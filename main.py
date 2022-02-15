import os
from crawl import get_ranking
from format import to_html

    :param content: email 내용

if __name__ == '__main__':
	url = "https://search.musinsa.com/ranking/keyword"
	send_to = os.environ['EMAIL_ADDRESS_TO']
	
	keyword_rank = get_ranking(url)
	content = to_html(keyword_rank, now)
