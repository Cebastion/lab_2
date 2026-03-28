# lab02_main.py
# Основна програма для обробки показників Фітнес-браслета

import stats_module as sm

def parse_input(input_str):
    """Перетворює введений рядок на список дійсних чисел"""
    try:
        values = [float(x) for x in input_str.strip().split()]
        return values
    except ValueError:
        print("Помилка: введено нечислові значення!")
        return None

def create_data_dict(pulse_list, steps_list, calories_list):
    """Формує словник даних з мітками часу"""
    n = len(pulse_list)
    data = {
        "pulse": {f"T{i+1}": pulse_list[i] for i in range(n)},
        "steps": {f"T{i+1}": steps_list[i] for i in range(n)},
        "calories": {f"T{i+1}": calories_list[i] for i in range(n)}
    }
    return data

def process_measurements(title, data_dict, threshold):
    """Виводить таблицю та статистику для заданого виду даних"""
    sm.show_table(data_dict, title)
    avg = sm.get_average(data_dict)
    min_val = sm.get_min(data_dict)
    max_val = sm.get_max(data_dict)
    median = sm.get_median(data_dict)
    jumps = sm.find_jumps(data_dict, threshold)
    
    print(f"\nСереднє значення: {avg}")
    print(f"Мінімум: {min_val}")
    print(f"Максимум: {max_val}")
    print(f"Медіана: {median}")
    
    if jumps:
        print("Різкі перепади:")
        for j in jumps:
            print(f"  {j}")
    else:
        print("Різких перепадів немає.")

def main():
    print("=== Обробка показів системи 'Фітнес-браслет' ===")
    
    pulse_input = input("Введіть пульс (уд/хв): ")
    steps_input = input("Введіть кроки (од): ")
    calories_input = input("Введіть калорії (ккал): ")

    pulse_list = parse_input(pulse_input)
    steps_list = parse_input(steps_input)
    calories_list = parse_input(calories_input)

    if not pulse_list or not steps_list or not calories_list:
        print("Помилка введення. Програма завершена.")
        return

    if not (len(pulse_list) == len(steps_list) == len(calories_list)):
        print("Помилка: кількість значень не збігається!")
        return

    data = create_data_dict(pulse_list, steps_list, calories_list)

    process_measurements("Pulse (уд/хв)", data["pulse"], 30)
    process_measurements("Steps (од)", data["steps"], 500)
    process_measurements("Calories (ккал)", data["calories"], 50)

if __name__ == "__main__":
    main()