"""モジュール内で使うUtils"""
from scipy.signal import argrelextrema
import numpy as np


class Utils:
    """Utils class"""

    @classmethod
    def get_local_min(self, array):
        """極小値"""
        index = argrelextrema(array, np.less)[0]
        return index

    @classmethod
    def get_local_max(self, array):
        """極大値"""
        index = argrelextrema(array, np.greater)[0]
        return index
