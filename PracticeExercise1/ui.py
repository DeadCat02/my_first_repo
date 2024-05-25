from logger import input_data, print_data, edit_data, delete_data

def interface():
    print('Добрый день, вы попали в специальный бот \n 1- запись \n 2- вывод данных \n 3 - редактирование \n 4 - удаление')
    command = int(input('Введите число: '))

    while command != 1 and command != 2 and command !=3 and command !=4:
        print("Неправильный ввод")
        command = int(input('Введите число: '))

    if command == 1:
        input_data()
    if command == 2:
        print_data()
    if command == 3:
        edit_data()
    if command == 4:
        delete_data()   