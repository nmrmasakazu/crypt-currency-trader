"""仮想通貨のAPIモジュール"""
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
import requests
import pandas as pd
from datetime import datetime
import datetime as dt
import time

from matplotlib import pyplot as plt
# https://github.com/matplotlib/mplfinance


class Api:
    """Api"""

    _REQUEST_URL = "https://api.cryptowat.ch/markets/bitflyer/btcjpy/ohlc"

    def __init__(self):
        """Init"""
        pass

    def get_price(self, period: int, plt_show: bool):
        """
        現在時間から1時間前までのデータを取得

        :param period: 何秒足か
        :param plt: グラフを表示するかどうか
        :return: pd.DataFrame
        """
        before_hour = 1
        before_min = 0
        now = datetime.now()
        y, m, d, h, mi = now.year, now.month, now.day, now.hour, now.minute
        params = RequestParams(periods=period,
                               before=self._unix_time(y, m, d, h, mi),
                               after=self._unix_time(y, m, d,
                                                     h - before_hour,
                                                     mi - before_min))
        response = requests.get(self._REQUEST_URL, params=params)
        response = response.json()["result"][str(period)]

        time, open_val, high_val, low_val, close_val = [], [], [], [], []
        for res in response:
            time.append(res[0])
            open_val.append(res[1])
            high_val.append(res[2])
            low_val.append(res[3])
            close_val.append(res[4])

        response_df = pd.DataFrame({'time': time,
                                    'open': open_val,
                                    'high': high_val,
                                    'low': low_val,
                                    'close': close_val})

        if plt_show:
            # Thanks https://qiita.com/p_q/items/883fd45c4bd3eb50fcb3
            date_axis = [datetime(y, m, d, h - before_hour, mi - before_min)
                         + dt.timedelta(minutes=minutes)
                         for minutes in range(before_hour * 60 + before_min)]
            ohlc = zip(mdates.date2num(date_axis),
                       open_val, high_val, low_val, close_val)

            ax = plt.subplot()
            ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
            candlestick_ohlc(ax, ohlc, width=(1 / 24 / 60)
                             * 0.7, colorup="g", colordown="r")
            plt.show()

        return response_df

    def _unix_time(self, y, m, d, h, mi):
        time_tuple = datetime(y, m, d, h, mi).timetuple()
        return int(time.mktime(time_tuple))


class RequestParams(dict):
    """リクエストのパラメータ"""

    __getattr__ = dict.get


# api = Api()
# api.get_price(period=300)
# print(api._unix_time(2018, 3, 28, 17))
