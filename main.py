def merge_sort(L): # "разделяй"
    if len(L) < 2: # если кусок массива меньше 2,
        return L[:] # выходим из рекурсии
    else:
        middle = len(L) // 2 # ищем середину
        left = merge_sort(L[:middle]) # рекурсивно делим левую часть
        right = merge_sort(L[middle:]) # и правую
        return merge(left, right) # выполняем слияние

def merge(left, right): # "властвуй"
    result = [] # результирующий массив
    i,j = 0,0 # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

def binary_search(L, element, left, right):
    if left > right: # если левая граница превысила правую,
        return False # значит элемент отсутствует

    middle = (right+left) // 2 # находимо середину
    if L[middle] == element: # если элемент в середине,
        return middle # возвращаем этот индекс
    elif element < L[middle]: # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(L, element, left, middle-1)
    else: # иначе в правой
        return binary_search(L, element, middle+1, right)


try:
    L = list(map(int, input('Введите последовательность чисел через пробел: ').split()))
    element = int(input('Введите произвольное число: '))

    merge_sort(L)
    if L[0] == L[-1]:
        print('Вы ввели только одно число! Необходимо ввести несколько чисел через пробел')
    elif element <= L[0] or element >= L[-1]:
        print(f'Введённое "произвольное число" не соответсвует условиям ввода значений списка от {L[0]} до {L[-1]}')
    else:
        print(binary_search(L, element, L[0], L[-1]))

except:
    print('Должны быть введены только числа через пробел! Попробуйте осуществить ввод повторно.')
