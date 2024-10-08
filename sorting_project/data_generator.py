import random

def generate_data(size, data_type='random'):
    # встановлюємо великий діапазон значень для випадкових чисел
    max_value = size * 10

    if data_type == 'random':
        # генеруємо випадкові числа з великого діапазону та можливими повторами
        return [random.randint(0, max_value) for _ in range(size)]
    elif data_type == 'sorted':
        # генеруємо випадковий список, а потім сортуємо його
        data = [random.randint(0, max_value) for _ in range(size)]
        return sorted(data)
    elif data_type == 'reversed':
        # генеруємо випадковий список, сортуємо в зворотньому порядку
        data = [random.randint(0, max_value) for _ in range(size)]
        return sorted(data, reverse=True)
    else:
        raise ValueError("Некоректний тип даних. Використовуйте 'random', 'sorted' або 'reversed'.")