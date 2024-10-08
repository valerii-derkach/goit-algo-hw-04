import time
import sys

from data_generator import generate_data

from sorting_algorithms.insertion_sort import insertion_sort
from sorting_algorithms.insertion_sort_recursive import insertion_sort_recursive
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.merge_sort_recursive import merge_sort_recursive
from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.bubble_sort_recursive import bubble_sort_recursive
from sorting_algorithms.quick_sort import quick_sort
from sorting_algorithms.quick_sort_iterative import quick_sort_iterative

def measure_time(func, data, is_in_place=True):
    start_time = time.perf_counter()
    if is_in_place:
        func(data)
        sorted_data = data
    else:
        sorted_data = func(data)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time, sorted_data

def main():
    sizes = [1000, 5000, 25000]  # змінити розміри за потребою
    data_types = ['random', 'sorted', 'reversed']

    # словник з алгоритмами сортування
    algorithms = {
        'Insertion Sort': (insertion_sort, True),
        'Insertion Sort Recursive': (insertion_sort_recursive, True),
        'Merge Sort': (merge_sort, False),
        'Merge Sort Recursive': (merge_sort_recursive, False),
        'Bubble Sort': (bubble_sort, True),
        'Bubble Sort Recursive': (bubble_sort_recursive, True),
        'Quick Sort': (quick_sort, False),
        'Quick Sort Iterative': (quick_sort_iterative, True),
        'Timsort (sorted)': (sorted, False)
    }

    # вибір алгоритмів для тестування
    selected_algorithms = [
        'Insertion Sort',
        'Insertion Sort Recursive',
        'Merge Sort',
        'Merge Sort Recursive',
        'Bubble Sort',
        'Bubble Sort Recursive',
        'Quick Sort',
        'Quick Sort Iterative',
        'Timsort (sorted)'
    ]

    # selected_algorithms = [
    #     'Insertion Sort',
    #     'Merge Sort',
    #     'Quick Sort',
    #     'Timsort (sorted)'
    # ]

    for size in sizes:
        print(f"\nРозмір масиву: {size}")
        for data_type in data_types:
            print(f"\nТип даних: {data_type}")
            original_data = generate_data(size, data_type)
            for name in selected_algorithms:
                func, is_in_place = algorithms[name]
                data = original_data.copy()
                try:
                    elapsed_time, sorted_data = measure_time(func, data, is_in_place)
                    is_correct = sorted_data == sorted(original_data)
                    print(f"{name}: {elapsed_time:.6f} секунд, Відсортовано правильно: {is_correct}")
                except RecursionError:
                    print(f"{name}: Перевищено глибину рекурсії для розміру {size}")
                except Exception as e:
                    print(f"{name}: Помилка - {e}")

if __name__ == "__main__":
    sys.setrecursionlimit(100000)  # збільшуємо ліміт рекурсії
    main()
