import json


def wr(book):
    with open('phonebook.json', 'w') as file:
        json.dump(book, file, indent=4)


with open('phonebook.json') as file:
    address_book = json.load(file)

while True:
    with open('phonebook.json') as file:
        address_book = json.load(file)
    wr(address_book)

    print('============================================================')
    info = input("Якщо ви хочете отримати контактну інформацію - натисніть 1 "
                 "\nЯкщо ви хочете додати контакт - натисніть 2 "
                 "\nЯкщо ви хочете видалити контакт - натисніть 3 "
                 "\nОтримати всі існуючі контакти - натисніть 4"
                 "\nОновити запис для заданого номера телефону - натисніть 5"
                 "\nЯкщо ви бажаете закінчити роботу - натисніть 0 \n"
                 "============================================================")

    if info == '1':
        inf = input("Введіть ім'я, прізвище, номер або місто людини, контакт якої бажаєте знайти:  "
                    "============================================================")
        tf_name = True
        count = 0
        for item in address_book:
            for elem in item:
                if item[elem] == inf:
                    tf_name = False
                    for key in item:
                        print(key + ': ' + item[key])
                    print("============================================================")
        if tf_name is True:
            print('Такого контакту не знайдено')

    elif info == '2':
        tf_name = True
        tf_surname = True

        name = input("Введіть ім'я: ").lower()
        surname = input("Введіть прізвище: ").lower()
        number = input("Введіть номер: ")
        city = input("Місто: ").lower()

        for item in address_book:
            for elem in item:
                if item[elem] == name:
                    tf_name = False
                if item[elem] == surname:
                    tf_surname = False

        if tf_name is True and tf_surname is True:
            address_book.append({'name': name, 'surname': surname, 'number': number, 'city': city})
            print('============================================================')
            print("Контакт створено")
            print('============================================================')
        else:
            tf_name = True
            tf_surname = True
            print('============================================================')
            print("Такий контакт вже існує")
            print('============================================================')

    elif info == '3':
        num = input("Введіть номер телефону людини, контакт якого бажаєте видалити: ")
        for i in range(len(address_book)-1):
            if address_book[i]['number'] == str(num):
                address_book.remove(address_book[i])
                wr(address_book)
                print('============================================================')
                print("Контакт " + num + ' ' + " видалено")
                print('============================================================')
            if i == len(address_book)-2:
                if num.isdigit():
                    print('Такий номер не знайдено')
                else:
                    print('Номер введено не корректно')

    elif info == '4':
        for item in address_book:
            for elem in item:
                print(elem + ': ' + item[elem])
            print('============================================================')

    elif info == '5':
        old_num = input('Номер: ')
        for i in range(len(address_book) - 1):
            if address_book[i]['number'] == str(old_num):
                number = input('Введіть новий номер: ')
                address_book[i]['number'] = number
                name = input("Введіть нове ім'я: ").lower()
                address_book[i]['name'] = name
                surname = input("Введіть нове прізвище: ").lower()
                address_book[i]['surname'] = surname
                city = input("Введіть нове місто: ").lower()
                address_book[i]['city'] = city
            else:
                print('Номер не знайдено')
        wr(address_book)
    else:
        print("Бувай")
        break
