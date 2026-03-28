import statistics

def get_average(data_dict):
    values = list(data_dict.values())
    return round(statistics.mean(values), 2) if values else None

def get_min(data_dict):
    values = list(data_dict.values())
    return min(values) if values else None

def get_max(data_dict):
    values = list(data_dict.values())
    return max(values) if values else None

def get_median(data_dict):
    values = list(data_dict.values())
    return statistics.median(values) if values else None

def find_jumps(data_dict, threshold):
    jumps = []
    keys = list(data_dict.keys())
    values = list(data_dict.values())
    for i in range(len(values)-1):
        diff = abs(values[i+1] - values[i])
        if diff > threshold:
            jumps.append(f"{keys[i]} → {keys[i+1]}: {diff}")
    return jumps

def show_table(data_dict, title):
    print(f"\n=== Таблиця показів: {title} ===")
    print(f"{'Мітка часу':<8} | {'Значення'}")
    print("-"*20)
    for key, value in data_dict.items():
        print(f"{key:<8} | {value}")