def func1(list1):
    min_number = min(list1)
    print(min_number)


def func2(my_dict, value):
    keys_list = []
    for j in my_dict.keys():
        if value == my_dict[j]:
            c = j
            keys_list.append(c)
    return keys_list


def func3(my_list):
    result_list = []
    for i in my_list:
        if type(i) == str:
            a = int(i)
            result_list.append(a)
        else:
            for b in i:
                result_list.append(b)
    result_list.sort(reverse=True)
    return result_list


print('1. Определение минимального числа среди элементов списка')
list1 = [-15.5, -12.5, 0, 5]
func1(list1)

print('\n2. Cписок ключей словаря, значения которых совпадают со значениями второго аргумента.\nЗначения - наименования'
      ' операторов.')
a_dict = {1: '+', 2: '-', 3: '*', 4: '/', 5: '+', 6: '+', 7: '*', 8: '*', 9: '*'}
value = input('Введите значение ключа: ')
print('Список ключей:', func2(a_dict, value))

print('\n3. Преобразование каждого элемента заданного списка a_list в целое число и сортировка полученного списка.')
a_list = ['1', '2', '-1', '10', [11, 22, 31, 24, 5, -6, 17, 68, -9, 0], '50', [90, 91, 100]]
print('Отсортированный по убыванию список:', func3(a_list))

print('\n4. Компиляция и выполнение фрагментов кода')
var = 10
compile_obj = compile('var', 'Value', 'single')
exec(compile_obj)