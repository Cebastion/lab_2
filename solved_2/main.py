from sensors import get_average, get_min, get_max, get_median, find_jumps, show_table

def parse_input(input_str):
    try:
        return [float(x) for x in input_str.strip().split()]
    except ValueError:
        print("Помилка: введено нечислові значення!")
        return None

def create_data_dict(pulse_list, steps_list, calories_list):
    n = len(pulse_list)
    return {
        "pulse": {f"T{i+1}": pulse_list[i] for i in range(n)},
        "steps": {f"T{i+1}": steps_list[i] for i in range(n)},
        "calories": {f"T{i+1}": calories_list[i] for i in range(n)}
    }

def process_measurements(title, data_dict, threshold):
    show_table(data_dict, title)
    print(f"Середнє значення: {get_average(data_dict)}")
    print(f"Мінімум: {get_min(data_dict)}")
    print(f"Максимум: {get_max(data_dict)}")
    print(f"Медіана: {get_median(data_dict)}")
    
    jumps = find_jumps(data_dict, threshold)
    if jumps:
        print("Різкі перепади:")
        for j in jumps:
            print(f"  {j}")
    else:
        print("Різких перепадів немає.")

def process_all(data):
    """Обробляє усі три види даних послідовно"""
    process_measurements("Pulse (уд/хв)", data["pulse"], 30)
    process_measurements("Steps (од)", data["steps"], 500)
    process_measurements("Calories (ккал)", data["calories"], 50)

def main():
    print("=== Обробка показів системи 'Фітнес-браслет' ===")

    pulse_list = parse_input(input("Введіть пульс (уд/хв): "))
    steps_list = parse_input(input("Введіть кроки (од): "))
    calories_list = parse_input(input("Введіть калорії (ккал): "))


    if not pulse_list or not steps_list or not calories_list:
        print("Помилка введення. Програма завершена.")
        return

    if not (len(pulse_list) == len(steps_list) == len(calories_list)):
        print("Помилка: кількість значень не збігається!")
        return

    data = create_data_dict(pulse_list, steps_list, calories_list)


    process_all(data)

if __name__ == "__main__":
    main()