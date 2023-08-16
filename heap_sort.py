# Пирамидальная сортировка (Сортировка кучей)

def heap_sort(list):
    size = len(list)
    build_max_heap(list, size)
    for i in range(size - 1, 0, -1):
        list[i], list[0] = list[0], list[i]
        max_heapify(list, i, 0)


def build_max_heap(list, size):
    for i in range(size, -1, -1):
        max_heapify(list, size, i)


def max_heapify(list, size, i):
    maxi = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < size and list[i] < list[left]:
        maxi = left
    if right < size and list[maxi] < list[right]:
        maxi = right
    if maxi != i:
        list[i], list[maxi] = list[maxi], list[i]
        max_heapify(list, size, maxi)

 
list = input('Введите список чисел через пробел: ').split()
list = [int(x) for x in list]
heap_sort(list)
print('Отсортированный список: ', end='')
print(list)
