"""グラフとして可視化するモジュール"""
from crypt_currency.utils import Utils
import matplotlib.pyplot as plt
import numpy as np


class Plot:
    """Plot class"""

    def show_moving_avg(self, val_df):
        """移動平均を表示"""
        # 終値でプロット
        plt.plot(val_df["close"], "k", label="closing")
        # 移動平均でプロット
        moving_average = val_df["close"].rolling(window=10).mean()
        plt.plot(moving_average, "b", label="moving avg")
        # 極大値
        local_maxs = Utils.get_local_max(np.array(moving_average))
        for local_max in local_maxs:
            plt.vlines(local_max, val_df["close"].min(),
                       val_df["close"].max(), "green", linestyles="dashed")
        # 極小値
        local_mins = Utils.get_local_min(np.array(moving_average))
        for local_min in local_mins:
            plt.vlines(local_min, val_df["close"].min(),
                       val_df["close"].max(), "red", linestyles="dashed")
        plt.legend()
        plt.show()

    def show_grad(self, val_df):
        """傾きのグラフ"""
        # 移動平均でプロット
        moving_average = val_df["close"].rolling(window=10).mean()
        # 数値勾配
        grad = np.gradient(moving_average)
        plt.plot(grad, "k", label="grad")
        plt.plot([0 for _ in range(len(grad))], "b", label="threshold")
        plt.legend()
        plt.show()
