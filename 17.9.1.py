numbers = input("Введите последовательность чисел через пробел: ")
numbers_list = [int(i) for i in numbers.split()]

if (' ' not in (numbers)):
    print('Введены некорректные данные!')
    numbers = input("Введите последовательность чисел через пробел: ")

num = int(input("Введите любое число: "))
if num % 1 == 0:
    numbers_list.append(num)
    print("Список до сортировки: ", numbers_list)
elif num % 1 != 0:
    print("Введены некорректные данные!")
    num = int(input("Введите любое число: "))

def my_sort(numbers_list):
    for i in range(len(numbers_list)):
        idx_min = i
        for j in range(i, len(numbers_list)):
            if numbers_list[j] < numbers_list[idx_min]:
                idx_min = j
        if i != idx_min:
            numbers_list[i], numbers_list[idx_min] = numbers_list[idx_min], numbers_list[i]
    return numbers_list

print("Список после сортировки:", my_sort(numbers_list))
