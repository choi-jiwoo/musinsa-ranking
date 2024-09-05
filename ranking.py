from datetime import datetime
from bs4 import BeautifulSoup as bs
import re
import requests
from user_agent import generate_user_agent
import pandas as pd


class MusinsaRanking:

    def __init__(self, url: str, max_count: int=20) -> None:
        self.url = url
        self.max_count = max_count
        self.headers = {
            'User-Agent': generate_user_agent(),
            'X-Requested-With': 'XMLHttpRequest',
        }

    def _get_request(self) -> requests.Response:
        res = requests.get(self.url, headers=self.headers)
        if res.status_code != 200:
            res.raise_for_status()
        return res

    def get_ranking(self) -> pd.DataFrame:
        res = self._get_request()
        data = res.json()
        item_list = data['data']['list']

        item = []
        status = []
        change = []

        for item_ in item_list[:self.max_count]:
            item.append(item_['keyword'])
            rank_change = item_['rankIncrement']
            if rank_change == 0:
                rank_change = '-'
                change_icon = rank_change
            elif rank_change > 0:
                change_icon = '▲'
            elif rank_change < 0:
                change_icon = '▼'

            status.append(change_icon)
            change.append(rank_change)

        item_mapping = list(zip(item, status, change))
        ranking = pd.DataFrame(item_mapping,
                               columns=['Item', 'Status', 'Change'])
        ranking.index += 1
        return ranking
