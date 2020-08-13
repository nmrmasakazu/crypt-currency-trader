"""売り・待機・買いのアルゴリズムモジュール"""
from crypt_currency.utils import Utils
import numpy as np


class BuySell:
    """アルゴリズム"""

    def predict(self, val_df):
        """
        予測

        :param val_df: 1時間分のOLHC
        :type val_df: pd.DataFrame
        :return: 'Y2C', 'C2Y' or 'DRAW'
        :rtype: str
        """
        # 売り買い指数
        buy_indicator = 0
        sell_indicator = 0

        # 移動平均
        moving_average = val_df["close"].rolling(window=10).mean()
        # 極大値
        local_maxs = Utils.get_local_max(np.array(moving_average))
        for local_max in local_maxs:
            if local_max > 58:
                sell_indicator += local_max
        local_maxs.max
        # 極小値
        local_mins = Utils.get_local_min(np.array(moving_average))
        for local_min in local_mins:
            if local_min > 58:
                buy_indicator += local_min

        # 結果
        if buy_indicator == sell_indicator:
            return 'DRAW'
        elif buy_indicator > sell_indicator:
            # 買い - 自分の現金は減少
            return 'Y2C'
        else:
            # 売り - 自分の現金は増加
            return 'C2Y'
