import random
from collections.abc import Hashable

print('1. Создание множества с помощью конструктора.')
a_set = set([x for x in range(1, 30, 3)])
print('a_set:', a_set)

print('\n2. Создание объекта, содержающий не менее трех элементов, имеющихся в объекте a_set. '
      'Проверка элементов на хэшируемость.')
it_ob = random.sample(a_set, 3)
print('it_ob:', it_ob)
for i in it_ob:
    if isinstance(i, Hashable):
        print(i, '- хэшируемый')
    else:
        print('Неизвестная ошибка')
#  Элементы во множестве не могут быть нехэшируемым, поэтому операция замены элемента не нужна.

print('\n3. Преобразование объекта it_ob в множество b_set и выполнение над множествами a_set и b_set операции.')
b_set = set(it_ob)
print('Метод intersection():', a_set.intersection(b_set))

print('\n4. Создание словаря a_dict с помощью литерала.')
a_dict = {'М. А. Булгаков': 'Мастер и Маргарита', 'Ф. М. Достоевский': 'Преступление и наказание',
          'Л. Н. Толстой': 'Война и мир', 'М. Ю. Лермонтов': 'Герой нашего времени'}
print('a_dict:', a_dict)

print('\n5. Выполнение методов словаря a_dict.')
print('Метод items():', a_dict.items())
print('Метод a_dict.popitem():', a_dict.popitem())
b_dict = {'А. С. Пушкин': 'Капитанская дочка'}
a_dict.update(b_dict)
print('Метод update():', a_dict)