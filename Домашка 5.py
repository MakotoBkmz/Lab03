user_name = input('Enter your name >>> ').title().strip(' 1234567890\t').replace(' ', '')
user_surname = input('Enter your surname >>> ').upper().strip(' 1234567890\t').replace(' ', '')

template = f'Привет {user_name} {user_surname} а ты знаешь что твоё имя состоит из 6 букв'

template_replacer = template.replace('Привет', 'Здарова')

print(template_replacer, end='?')
