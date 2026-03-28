# stats_module.py
# Модуль із підпрограмами для статистичної обробки показників

import statistics

def get_average(data_dict):
    """Повертає середнє значення"""
    values = list(data_dict.values())
    if not values:
        return None
    return round(statistics.mean(values), 2)

def get_min(data_dict):
    """Повертає мінімальне значення"""
    values = list(data_dict.values())
    if not values:
        return None
    return min(values)

def get_max(data_dict):
    """Повертає максимальне значення"""
    values = list(data_dict.values())
    if not values:
        return None
    return max(values)

def get_median(data_dict):
    """Повертає медіану"""
    values = list(data_dict.values())
    if not values:
        return None
    return statistics.median(values)

def find_jumps(data_dict, threshold):
    """Знаходить різкі перепади між сусідніми значеннями"""
    jumps = []
    keys = list(data_dict.keys())
    values = list(data_dict.values())
    for i in range(len(values) - 1):
        diff = abs(values[i+1] - values[i])
        if diff > threshold:
            jumps.append(f"{keys[i]} → {keys[i+1]}: {diff}")
    return jumps

def show_table(data_dict, title):
    """Виводить таблицю значень"""
    print(f"\n=== Таблиця показів: {title} ===")
    print(f"{'Мітка часу':<8} | {'Значення'}")
    print("-"*20)
    for key, value in data_dict.items():
        print(f"{key:<8} | {value}")