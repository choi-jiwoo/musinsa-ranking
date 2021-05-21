import datetime
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from crawl import get_ranking
from format import to_html

def send_email(send_to, content):
    """
    :param send_to: 수신자 email
    :param content: email 내용
    """
    sent_from = os.environ['EMAIL_ADDRESS_FROM']
    pw = os.environ['EMAIL_PW']
    
    # 서버 연결
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sent_from, pw)

    # 메일로 보낼 내용
    msg = MIMEMultipart()
    msg['Subject'] = str("무신사 스토어 {} 검색어 랭킹".format(now))
    part = MIMEText(content, "html")
    msg.attach(part)
    msg['To'] = send_to
    smtp.sendmail(sent_from, send_to, msg.as_string())


if __name__ == '__main__':
	url = "https://search.musinsa.com/ranking/keyword"
	send_to = os.environ['EMAIL_ADDRESS_TO']
	
    # YYYY MM DD 00시 날짜 포맷
	now = datetime.datetime.now()
	now = now.strftime('%Y %m %d %H시')

	keyword_rank = get_ranking(url)
	content = to_html(keyword_rank, now)
	send_email(send_to, content)
