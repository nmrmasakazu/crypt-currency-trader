"""売り・待機・買いのアルゴリズムモジュール"""
from crypt_currency.utils import Utils
import numpy as np


class BuySell:
    """アルゴリズム"""

    def predict(self, val_df):
        """予測"""
        # 売り買い指数
        buy_indicator = 0
        sell_indicator = 0
        # 移動平均
        moving_average = val_df["close"].rolling(window=10).mean()
        # 極大値
        local_maxs = Utils.get_local_max(np.array(moving_average))
        for local_max in local_maxs:
            if local_max > 55:
                sell_indicator += 1
        # 極小値
        local_mins = Utils.get_local_min(np.array(moving_average))
        for local_min in local_mins:
            if local_min > 55:
                buy_indicator += 1

        # 結果
        if buy_indicator == sell_indicator:
            return None
        elif buy_indicator > sell_indicator:
            # 買い - 自分の現金は減少
            return -val_df["close"][len(val_df) - 1]
        else:
            # 売り - 自分の現金は増加
            return val_df["close"][len(val_df) - 1]
