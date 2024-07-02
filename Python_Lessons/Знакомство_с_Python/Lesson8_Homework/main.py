def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('file.txt')
    while (choice!=7):

        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('Фамилия: ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            phone_number=input('Номер телефона: ')
            print(find_by_number(phone_book, phone_number))
        elif choice==4:
            user_data=input('Введите данные (формат "[фамиля], [имя], [номер], [описание]"): ')
            phone_book = add_user(phone_book, user_data)
            write_txt('file.txt',phone_book)
        elif choice==5:
            print_result(phone_book)
            string_num = int(input('\n Какой по счету контакт перенести?: ')) - 1
            transfer_string(phone_book, string_num)
        elif choice==6:
            exit()

        choice=show_menu()

def print_result(phb):
    for i in phb:
        for k,v in i.items():
            print(f"{k}:{v}")

def find_by_lastname(phb, last_name):
    for i in phb:
        if(last_name in i.values()):
            print("Найдено!")
            for k,v in i.items():
                print(f"{k}:{v}")

def find_by_number(phb, number):
    for i in phb:
        if(f'{number}' in i.values()):
            print("Найдено!")
            for k,v in i.items():
                print(f"{k}:{v}")

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data.split(', ')))
    phone_book.append(record)
    return phone_book


def show_menu():
    print("\n Выберите необходимое действие\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник \n"
          "5. Перенести строку в другой файл\n"
          "6. Закончить работу")
    choice = int(input())
    return choice




def read_txt(filename): 
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
           if line == '':
               record = dict(zip(fields, ['', '', '', '']))
               continue
           record = dict(zip(fields, line.split(', ')))
           phone_book.append(record)
    return phone_book


def write_txt(filename, phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        text = ''
        phone_book = clean_from_n(phone_book)
        for i in phone_book:
            for k, v in i.items():
                if(k == 'Описание' and i == phone_book[-1]):
                    text = text + v 
                elif(k == 'Описание'):
                    text = text + v + '\n' 
                else:
                    text = text + v + ', '
        phout.write(text)


def transfer_string(phone_book, string_num):
    phone_book_2 = read_txt('file2.txt') #Сохраняем в этму переменную телефонный справочник со второго файла
    string = phone_book[string_num] #Та строка, которая нам нужно добавить из первого файла
    phone_book_2.append(string) #Добавляем эту строку
    with open('file2.txt', 'w',encoding='utf-8') as phout:
        text = ''
        phone_book_2 = clean_from_n(phone_book_2) #Очищаем от всех \n
        for i in phone_book_2:
            for k, v in i.items():
                if(k == 'Описание' and i == phone_book_2[-1]):
                    text = text + v 
                elif(k == 'Описание'):
                    text = text + v + '\n' 
                else:
                    text = text + v + ', '
        phout.write(text)

def clean_from_n(phone_book): #Эта функция убирает все \n которые есть в справочнике, т.к. они все портят
    for i in range(len(phone_book)):
        for k,v in phone_book[i].items():
            phone_book[i][k] = v.replace('\n', '')
    return phone_book

work_with_phonebook()