def partition(array, left, right):
    i = (left - 1)
    pivot = array[right]
    for j in range(left, right):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]
    return (i + 1)

def quick_sort_iterative(array):
    left = 0
    right = len(array) - 1
    # Створити допоміжний стек
    size = right - left + 1
    stack = [0] * size

    # ініціалізувати верхівку стеку
    top = -1

    # додати початкові значення left та right до стеку
    top = top + 1
    stack[top] = left
    top = top + 1
    stack[top] = right

    # Продовжувати витягувати зі стеку, поки він не порожній
    while top >= 0:

        # Витягнути right і left
        right = stack[top]
        top = top - 1
        left = stack[top]
        top = top - 1

        # Встановити опорний елемент на його правильну позицію у відсортованому масиві
        pivot_position = partition(array, left, right)

        # Якщо є елементи з лівого боку від опорного елемента,
        # додати ліву частину до стеку
        if pivot_position - 1 > left:
            top = top + 1
            stack[top] = left
            top = top + 1
            stack[top] = pivot_position - 1

        # Якщо є елементи з правого боку від опорного елемента,
        # додати праву частину до стеку
        if pivot_position + 1 < right:
            top = top + 1
            stack[top] = pivot_position + 1
            top = top + 1
            stack[top] = right
