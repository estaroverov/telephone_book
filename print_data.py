import os.path
def print_all_data(data):
    if data == None:
        print("No such file!")
        return None
    if len(data) > 0:
        print("Фамилия".center(20), "Имя".center(20), "Отчество".center(20), "Дата рождения".center(20), "Телефон".center(15), "Категория".center(30))
        print("-"*130)
        print_data(data)
    else:
        print("Справочник пуст!")

def print_data(data):
    for item in data:
        print(item[0].center(20), item[1].center(20), item[2].center(20), item[3].center(20), item[4].center(15), item[5].center(30))

def print_found_rows(found):
    if found == None:
        print("No such file!")
        return None
    if found != None or found != []:
            print("Фамилия".center(20), "Имя".center(20), "Отчество".center(20), "Дата рождения".center(20), "Телефон".center(15), "Категория".center(30))
            print("-"*130)
            print_data(found)
    else:
        print("Данные не обнаружены")

