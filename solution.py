import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 264956206  # Ваш chat ID, не меняйте название переменной


def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    scale = 17
    alpha = 1 - p
    s_squared = np.sum(x**2)
    z1 = chi2.ppf(1 - alpha / 2, df=len(x) * 2)
    z2 = chi2.ppf(alpha / 2, df=len(x) * 2)
    left_border = np.sqrt(s_squared / (z1 * scale))
    right_border = np.sqrt(s_squared / (z2 * scale))
    return left_border, right_border
