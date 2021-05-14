import datetime
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from crawl import get_ranking
from format import to_html

def send_email(send_to, content):
    """
    :param send_to: email recipient
    :param content: email content
    """
    # email and password setting
    sent_from = os.environ['EMAIL_ADDRESS_FROM']
    pw = os.environ['EMAIL_PW']
    
    # connect to a server
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sent_from, pw)

    # content
    msg = MIMEMultipart()
    msg['Subject'] = str("무신사 스토어 {} 검색어 랭킹".format(now))
    part = MIMEText(content, "html")
    msg.attach(part)
    msg['To'] = send_to
    smtp.sendmail(sent_from, send_to, msg.as_string())


if __name__ == '__main__':
	url = "https://search.musinsa.com/ranking/keyword"
	send_to = os.environ['EMAIL_ADDRESS_TO']
	
	now = datetime.datetime.now()
	now = now.strftime('%Y %m %d %H시')

	keyword_rank = get_ranking(url)
	html_format = to_html(keyword_rank, now)
	send_email(send_to, html_format)
