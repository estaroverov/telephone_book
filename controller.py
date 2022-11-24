from import_data import import_data
from export_data import export_data
from print_data import *
from search_data import *


def greeting():
    print("Добро пожаловать в телефонный справочник!")


def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    brith_name = input("Введите дату рождения: ")
    phone_number = input("Введите номер контакта: ")
    note = input("Введите категорию контакта: ")
    return [last_name, first_name, middle_name, brith_name, phone_number, note]


def choice_sep():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep


def choice_todo():
    print("Доступные операции с телефонной книгой:\n\
    1 - импорт;\n\
    2 - экспорт;\n\
    3 - поиск контакта;\n\
    4 - поиск по столбцу")
    ch = input("Введите цифру: ")
    filename = input("Введите имя файла: ")
    if ch == '1':
        sep = choice_sep()
        import_data(input_data(),filename, sep)
    elif ch == '2':
        data = export_data(filename)
        print_all_data(data)
    elif ch == '3':
        word = input("Введите данные для поиска: ")
        data = export_data(filename)
        item = search_data(word, data)
        print_found_rows(item)
    elif ch =='4':
        word = input("Введите данные для поиска: ")
        data = export_data(filename)
        column = input("Введите номер столбца: ")
        item = search_val(word, data, column)
        print_found_rows(item)
    else:
        print("Нет такого пункта меню!")
