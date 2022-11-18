import view
import model

def start():
    view.menu()
    print(' ')
    number = int(input("Введите число и нажмите Enter: "))
    return number

def options(number):
    if number == 1:
        phonebook_output()
    elif number == 2:
        new_contact_controller()
    elif number == 3:
        html_created_controller()
    elif number == 4:
        data_reading()
    else:
        view.error()



def new_contact_controller():
    view.new_contact_example()
    new_contact = input('')
    model.new_contact_model(new_contact)
    model.alphabetical_overwriting(model.get_phonebook())
    view.new_contact_saved()


def html_created_controller():
    model.html_generator(model.html_list(model.alphabetical_sorting(model.get_phonebook())))
    view.html_created()

def phonebook_output():
    view.phonebook_output()

def data_reading():
    view.data_reading()

