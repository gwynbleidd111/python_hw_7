
def new_contact_model(new_contact):
    text_1 = open('phonebook.txt', 'a',encoding='utf-8')
    text_1.writelines(f'{new_contact}\n')
    text_1.close()

def get_phonebook():
    text = open('phonebook.txt', encoding='utf-8')
    phonebook = text.readlines()
    text.close()
    return phonebook

def alphabetical_overwriting(phonebook):
    text_1 = open('phonebook.txt', 'w',encoding='utf-8')
    sorted_phonebook = sorted(phonebook)
    text_1.writelines(sorted_phonebook)
    text_1.close()

def alphabetical_sorting(phonebook):
    sorted_phonebook = sorted(phonebook)
    return sorted_phonebook


def html_list(sorted_phonebook):
    sorted_phonebook_new = []
    for i in range(len(sorted_phonebook)):
        sorted_phonebook_new.append(f"<p>{sorted_phonebook[i]}</p>")
    sorted_phonebook_new = ''.join(sorted_phonebook_new)
    return sorted_phonebook_new

def html_generator(sorted_phonebook_new):
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>Телефонный справочник: {} </p>\n'\
        .format(style, html_list(sorted_phonebook_new))
    html += '  </body>\n</html>'
    with open('index.html', 'w') as page:
        page.write(html)
    return html

def phonebook_output(sorted_phonebook):
    sorted_phonebook =  ''.join([str(x) for x in sorted_phonebook]).title()
    return sorted_phonebook

