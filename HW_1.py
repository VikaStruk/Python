# 1 Создать переменную типа String
type_string = 'Hello'
print(type_string, type(type_string))

# 2 Создать переменную типа Integer
type_integer = 24
print(type_integer, type(type_integer))

# 3 Создать переменную типа Float
type_float = 1.5
print(type_float, type(type_float))

# 4 Создать переменную типа Bytes
type_bytes = b'123'
print(type_bytes, type(type_bytes))

# 5 Создать переменную типа List (список) ((массив)
type_list = [234, 'world', {'age': 24, 'name': 'Vika'}]
print(type_list, type(type_list))

# 6 Создать переменную типа Tuple (Кортежи, ) (неизменяемый список)
type_tuple = ('Good morning',)
print(type_tuple, type(type_tuple))

# 7 Создать переменную типа Set (изменяемое множество(контейнер)-выводит элементы множества БЕЗ будликатов
type_set = {12, 'privet', 'kak dela', 12}
print(type_set, type(type_set))

# 8 Создать переменную типа Frozen set (НЕизменяемое множество, нельзя добалять/удалять элементы)
type_frozenset = {'nika', 'pipa', 1234}
print(type_frozenset, type(type_frozenset))

# 9 Создать переменную типа Dict (словарь), ст-ра: ключ-значение
type_dict = {'Name': 'Vika', 'Age': 24}
print(type_dict, type(type_dict))

# 10 Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
first_string = 'Privet, '
second_string = 'Kak dela?'
third_string = (first_string + second_string)
print(third_string)

# 11 Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
# type_1 = 'I am'
# type_2 = 24
# print(type_1, type_2)

# 12 Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
type_1 = 'I am '
type_2 = 24
print(type_1 + str(type_2))