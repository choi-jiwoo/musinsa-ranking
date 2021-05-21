# 무신사 검색어 랭킹

Github Actions를 통해 무신사스토어 검색어 랭킹을 특정한 시간마다 이메일로 받을 수 있음

출처 : https://search.musinsa.com/ranking/keyword

### Github Actions

이메일 계정 정보를 repository secrets에 설정.

`main.yml`

### 파일

`main.py` - 이메일 전송

`crawl.py` - 검색어 크롤링

`format.py` - 이메일로 보낼 결과물 포맷 설정

### 필요한 패키지 설치

`$ pip install -r requirements`

### Gmail 보안 문제

구글 계정에 2단계 인증이 되어있고 '앱 비밀번호'를 생성한 후 '앱 비밀번호'를 이용해 로그인해야 함
