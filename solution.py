import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 264956206  # Ваш chat ID, не меняйте название переменной


def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    s_squared = np.sum((x - np.mean(x)) ** 2)
    left_border = np.sqrt(((s_squared) / (17 * chi2.ppf(1 - alpha / 2, len(x) - 1))))
    right_border = np.sqrt(((s_squared) / (17 * chi2.ppf(alpha / 2, len(x) - 1))))
    if left_border > right_border:
        return right_border, left_border
    return left_border, right_border
