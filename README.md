# 무신사 검색어 랭킹

Github Actions를 통해 무신사스토어 검색어 랭킹을 특정한 시간마다 이메일로 받을 수 있음

크롤링 데이터 출처 : https://search.musinsa.com/ranking/keyword

### Github Actions

이메일 계정 정보를 repository secrets에 추가하고 *Actions*탭에서 Workflow 생성

`main.yml`

```yml
run: |
  python main.py
env:
  # 이곳에 이메일 계정 관련 secrets 추가
  # 예)
  # username: ${{ secrets.username }}
```
