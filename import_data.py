# модуль импорта данных 

def import_data(data, sep=None):
    with open('phone.csv', 'a+',encoding='UTF-8') as file:
        if sep == None:
            file.write(','.join(data))
            file.write(f"\n")
        else:
            file.write(sep.join(data))
            file.write(f"\n")