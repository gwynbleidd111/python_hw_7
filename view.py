import model
def menu():
    print(' ')
    print('Это ваш телефонный справочник.\n\nНажмите:\n'+
'1 - для просмотра всех контактов\n2 - для записи нового контакта\n'+
'3 - для экспорта справочника в формат html\n4 - для чтения данных фйла')

def new_contact_example():
    print(' ')
    print('Введите новый контакт так, как указано в примере:"Антон: +79001111111"')

def new_contact_saved():
    print(' ')
    print('Новый контакт успешно сохранен.')

def html_created():
    print(' ')
    print("Справочник успешно экспортированн в формат html.")

def phonebook_output():
    print(' ')
    print('Телефонный справочник:')
    print(model.phonebook_output(model.alphabetical_sorting(model.get_phonebook())))

def error():
    print(' ')
    print('Ошибка!')

def data_reading():
    print(model.get_phonebook())
