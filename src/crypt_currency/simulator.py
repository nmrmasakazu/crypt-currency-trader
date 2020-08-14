"""シミュレーション売買を行うモジュール"""
import pandas as pd


class Simulator:
    """Simulator class"""

    def __init__(self, my_deposit):
        """
        Init

        :param: my_deposit: 最初にある現金 [yen]
        """
        self._my_amount = my_deposit
        self._my_btc = 0
        # 売買情報
        self._hists_title: [str] = []
        # 仮想通貨の日本円価値と現金の合計
        self._hists_current_yen: [float] = []
        # 売買した後の保有する現金
        self._hists_yen: [float] = []
        # 売買した後の保有する仮想通貨
        self._hists_btc: [float] = []

    def _record_hist(self, title, current_yen, yen, btc):
        self._hists_title.append(title)
        self._hists_current_yen.append(yen + current_yen * btc)
        self._hists_yen.append(yen)
        self._hists_btc.append(btc)

    def get_record_hist(self):
        """
        売買履歴を表示

        :return: pd.DataFrame
        """
        df = pd.DataFrame()
        df["title"] = self._hists_title
        df["total"] = self._hists_current_yen
        df["yen"] = self._hists_yen
        df["btc"] = self._hists_btc

        return df

    def _draw(self, current_yen):
        """何もしない，レコードに残すだけ"""
        self._record_hist("", current_yen, self._my_amount, self._my_btc)

    def _yen_to_btc(self, current_yen, btc):
        """円を仮想通貨に換金"""
        # 約定可能か
        if self._my_amount >= current_yen * btc:
            self._my_amount -= current_yen * btc
            self._my_btc += btc
            self._record_hist("Y2C", current_yen,
                              self._my_amount, self._my_btc)
        else:
            self._record_hist("", current_yen,
                              self._my_amount, self._my_btc)

    def _btc_to_yen(self, current_yen, btc):
        """仮想通貨を円に換金"""
        # 約定可能か
        if self._my_btc >= btc:
            self._my_amount += current_yen * btc
            self._my_btc -= btc
            self._record_hist("C2Y", current_yen,
                              self._my_amount, self._my_btc)
        else:
            self._record_hist("", current_yen,
                              self._my_amount, self._my_btc)

    def get_my_amount(self):
        """現在の現金額を取得"""
        return self._my_amount

    def get_my_btc(self):
        """現在の仮想通貨額を取得"""
        return self._my_btc

    def calc_pure_amounts(self, yen_per_btc):
        """現在のBTCを円にした時の価値"""
        return self._my_amount + self._my_btc * yen_per_btc

    def exec(self, action, current_yen):
        """
        売買を行うメインメソッド

        :param: action: Y2C, C2Y or DRAW
        :param: current_yencurrent_yen: 現在の日本円価格 [yen/btc]
        """
        if action == 'Y2C':
            self._yen_to_btc(current_yen=current_yen, btc=0.01)
        elif action == 'C2Y':
            self._btc_to_yen(current_yen=current_yen, btc=0.01)
        else:
            self._draw(current_yen=current_yen)
