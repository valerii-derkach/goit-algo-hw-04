import random
import sys
from data_generator import generate_data
from sorting_algorithms.merge_sort import merge

def generate_sorted_lists(k, min_size, max_size):
    sorted_lists = []
    for _ in range(k):
        size = random.randint(min_size, max_size)
        data = generate_data(size, data_type='sorted')
        sorted_lists.append(data)
    return sorted_lists

def merge_k_lists(lists):
    if not lists:
        return []
    if len(lists) == 1:
        return lists[0]
    
    mid = len(lists) // 2
    left_merged = merge_k_lists(lists[:mid])
    right_merged = merge_k_lists(lists[mid:])
    
    return merge(left_merged, right_merged)

if __name__ == "__main__":

    # sys.setrecursionlimit(10000)  # збільшуємо ліміт рекурсії, якщо потрібно

    k = 5  # кількість списків
    min_size = 5  # мінімальний розмір списку
    max_size = 15  # максимальний розмір списку

    lists = generate_sorted_lists(k, min_size, max_size)

    print("Згенеровані відсортовані списки:")
    for idx, lst in enumerate(lists):
        print(f"Список {idx + 1} (розмір {len(lst)}): {lst}")

    merged_list = merge_k_lists(lists)

    print("\nВідсортований змерджений список:")
    print(merged_list)
