import os
from smtp import Smtp
from ranking import MusinsaRanking
import argparse


def main(args):
    sex = args.sex.upper()
    url = f'https://ranking.musinsa.com/api/ranking/v1/page/keyword?sex={sex}'
    sender = os.environ['EMAIL_ADDRESS_FROM']
    sender_pw = os.environ['EMAIL_PW']
    receiver = os.environ['EMAIL_ADDRESS_TO']

    smtp = Smtp(sender, sender_pw)
    ranking = MusinsaRanking(url, args.count).get_ranking()
    smtp.send_mail(receiver, ranking)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--sex', type=str, default='A', help='A=All, M=Male, F=Female')
    parser.add_argument('--count', type=int, default=20)
    args = parser.parse_args()

    main(args)