# На отлично в одного человека надо сделать консольное приложение Телефонный справочник 
# с внешним хранилищем информации, и чтоб был реализован основной функционал - просмотр, 
# сохранение, импорт, поиск, удаление, изменение данных.


import json


def add(contact, contact_info):
    phonebook[contact] = contact_info
    print('Контакт успешно добавлен. Не забудьте его сохранить')
        
def save():
    f = open('contacts.json', 'a', encoding='utf-8')
    f.write(json.dumps(phonebook, ensure_ascii=False))
    f.close()
    print('Контакт успешно сохранен')

def load():
    try:
        f = open('contacts.json', 'r', encoding='utf-8')
        temp = json.loads(f.read())
        f.close()
        print('Загрузка успешно завершена')
    except:
        print('Загружен тестовый справочник')
        temp = {"Иван Сергеевич": {'phones': [3456789, 9217809191], 'birthday': "05.05.1959", 'e-mail': "Vania@mail.ru"},
             "Тетя Оля": {'phones': [7890000]}}
    return temp

def show():
    for name, values in phonebook.items():
                print(name, values)

def delete():
    key = input('Введите имя контакта, который нужно удалить: ')
    if key in phonebook == False:
        print('Такой контакт отсутствует')
    else:
        del phonebook[key]
        print('Контакт успешно удален')

def find_contact():  
    temp = phonebook.get(input('Введите имя контакта: '))
    if temp == None:
        print('Такой контакт отсутствует')
    else:
        print(temp)

def change_contact():
    temp = input('Введите имя контакта: ')
    phonebook[temp] = data1
    print('Изменения сохранены')


name = "Жека"
data = {'phones': [4569000, 89214567890], 'birthday': "07.03.1988", 'e-mail': "tip@mail.ru"}
data1 = {'phones': [2346787]}  
phonebook = load()
print(phonebook)
print()
print('Вам доступны следующие команды:\nadd - добавить контакт\nsave - сохранить контакт\ndelete - удалить контакт')
print('load - загрузить телефонный справочник\nshow - просмотреть список контактов\nfind - поиск контакта')
print('change - изменить контак\nexit - выход из телефонного справочника')
print()

while True:    
    print()
    command = input('Введите команду: ')
    match command:
        case "add":
           add(name, data)
        case "save":
            save()
        case "load":
            print(load())
        case "show":
            show()
        case "delete":
            delete()
        case "find":
            find_contact()
        case "change":
            change_contact()
        case "exit":
            answer = input("Вы уверены, что хотите выйти? (y/n): ")
            if answer == "y":
                break
        case _: 
            print('Такой команды не существует')
            

