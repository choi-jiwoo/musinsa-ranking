import datetime

def to_html(keyword_rank, now):
    """
    :param keyword_rank: 메일 내용에 추가할 dataframe
    :param now: 현재시각
    :return: html 포맷으로 된 내용
    """
    content = '<html>\n<body>\n'
    content += "<h3>"+str("무신사 스토어 {} 검색어 랭킹".format(now))+"</h3>\n"
    content += "<table>\n<tr>\n<th>순위</th>\n<th>키워드</th>\n<th colspan=\"2\">상승/감소</th>\n</tr>\n"

    for i in range(len(keyword_rank)):
        content += "<tr>\n"
        content += "<td>" + str(keyword_rank.index[i]) + "</td>\n"
        content += "<td>" + str(keyword_rank['Item'].iloc[i]) + "</td>\n"
        content += "<td>" + str(keyword_rank['Status'].iloc[i]) + "</td>\n"
        content += "<td>" + str(keyword_rank['Change'].iloc[i]) + "</td>\n"
        content += "</tr>\n"

    content += "</table>\n</body>\n</html>"
    return content