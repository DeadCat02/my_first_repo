from data_create import *

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные? \n \n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name}; {surname}; {phone}; {address}\n"
    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число: '))

    if var == 1:
        with open('data1.csv', 'a', encoding="utf-8") as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")

    if var == 2:
        with open('data2.csv', 'a', encoding="utf-8") as f:
            f.write(f"{name}; {surname}; {phone}; {address}\n")


def print_data():
    print('Вывожу первый файл: \n')
    with open('data1.csv', 'r', encoding="utf-8") as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i 
        print(''.join(data_first_list))

    print('Вывожу второй файл: \n')
    with open('data2.csv', 'r', encoding="utf-8") as f:
        data_second = f.readlines()
        print(*data_second)

def edit_data(): #Редактирование записей

    var1 = int(input("Какой файл отредактировать? \n 1 - первый файл \n 2 - второй файл \n Номер файла: "))
    while var1 !=1 and var1 !=2:
        print("Ошибка ввода, попробуйте еще раз: ")
        var1 = int(input("Какой файл отредактировать? \n 1 - первый файл \n 2 - второй файл \n Номер файла: "))
    
    if(var1 == 1): #Редактирование первого файла
        print('Вывожу первый файл: \n')
        with open('data1.csv', 'r', encoding="utf-8") as f:
            data_first = f.readlines()
            data_first_list = []
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_list.append(''.join(data_first[j:i+1]))
                    j = i 
            print(''.join(data_first_list))

        var2 = int(input("Какую по счету запись отредактировать?: "))

        content = []
        with open('data1.csv', 'r') as f: #Упорядоченно переносим содержание файла в переменную 'content'
            data_first = f.readlines()
            print(data_first)
            temp_list = []
            for i in data_first:
                if i == '\n':
                    content.append(temp_list)
                    temp_list = []
                    continue
                temp_list.append(i)
            if ('\n' in temp_list):
                temp_list.remove('\n')
            content.append(temp_list)
        
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()

        content[var2-1] = [name + "\n", surname + "\n", phone + "\n", address + "\n"] 
        print(content)
        if(var2 > len(content)):
            print("Неправильный номер записи!")
            exit()

        with open('data1.csv', 'w') as f: #Переносим содержимое переменной 'content' в файл
            for i in range(len(content)):
                for j in content[i]:
                    f.writelines(j)
                if (i!= len(content) - 1):
                    f.write("\n")

    if(var1 == 2): #Редактирование второго файла
        print('Вывожу второй файл: \n')
        with open('data2.csv', 'r', encoding="utf-8") as f:
            data_second = f.readlines()
            print(*data_second)

        var2 = int(input("Какую по счету запись отредактировать?: "))

        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()

        content = []
        with open('data2.csv', 'r') as f: #Отправляем заредактированные данные в переменную 'content', которая хранит всю инфу
            content = f.readlines()
            content[var2-1] = f"{name}; {surname}; {phone}; {address}\n"

        with open('data2.csv', 'w') as f: #Переносим содержание переменной 'content' в файл
            for i in content:
                f.write(i)   

def delete_data(): #Удаление записей
    
    var1 = int(input("C каким файлом работать? \n 1 - первый файл \n 2 - второй файл \n Номер файла: "))
    while var1 !=1 and var1 !=2:
        print("Ошибка ввода, попробуйте еще раз: ")
        var1 = int(input("C каким файлом работать? \n 1 - первый файл \n 2 - второй файл \n Номер файла: "))
    
    if(var1 == 1): #Удаление записи в первом файле
        print('Вывожу первый файл: \n')
        with open('data1.csv', 'r', encoding="utf-8") as f:
            data_first = f.readlines()
            data_first_list = []
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_list.append(''.join(data_first[j:i+1]))
                    j = i 
            print(''.join(data_first_list))

        var2 = int(input("Какую по счету запись удалить?: "))

        content = []
        with open('data1.csv', 'r') as f: 
            data_first = f.readlines()
            temp_list = []
            for i in data_first:
                if i == '\n':
                    content.append(temp_list)
                    temp_list = []
                    continue
                temp_list.append(i)
            if ('\n' in temp_list):
                temp_list.remove('\n')
            content.append(temp_list)

        print(content)

        del(content[var2-1])

        print(content)

        with open('data1.csv', 'w') as f:
            for i in range(len(content)):
                for j in content[i]:
                    f.writelines(j)
                if i != len(content) - 1:
                    f.write("\n")
                else:
                    f.write("\n \n")

    if(var1 == 2): #Удаление записи со второго файла
        print('Вывожу второй файл: \n')
        with open('data2.csv', 'r', encoding="utf-8") as f:
            data_second = f.readlines()
            print(*data_second)

        var2 = int(input("Какую по счету запись удалить?: "))
        content = []
        with open('data2.csv', 'r') as f: #Упорядоченно переносим содержание файла в переменную 'content'
            content = f.readlines()

        del(content[var2-1])

        with open('data2.csv', 'w') as f:
            for i in content:
                f.write(i)
