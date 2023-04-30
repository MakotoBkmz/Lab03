user_name = input('Enter your name >>> ').title().strip(' 1234567890\t').replace(' ', '')
user_surname = input('Enter your surname >>> ').upper().strip(' 1234567890\t').replace(' ', '')
letter_count = len(user_name)

template = f'Привет {user_name} {user_surname} а ты знаешь что твоё имя состоит из {letter_count} букв'

template_replacer = template.replace('Привет', 'Здарова')

format_method = template_replacer.format(user_name=user_name, user_surname=user_surname, letter_count=letter_count)

output = f'{format_method}?'

print(output)
