# очікуваний результат у вигляді: My name is David, I am 14 years old👣

# example
# f = '\N{Footprints}'  # not informative naming, the correct code below
smile_footprint = '\N{Footprints}'

User_name = input('Please, enter your name >>> ').title()
'''
User_name should not have Space between '_' and 'name' 
Inside 'input' brackets should be pointed out the info user has to type
For convenience we should add '.title() after ')'
'''
User_age = input('Please, enter your age >>> ')
'''
Should have space between '=' and 'input'
Should not have space between 'input' and '('
'''
#Result = 'My name is ' + User_name + ", I am " + User_age + 'years old' + smile_footprint
Result = f'My name is {User_name}, I am {User_age} years old{smile_footprint}'
'''
Code cannot be done in cyrillic. (Результат - Result)
Whole string should not have that much pluses, so use 'f-string' instead
'''

print(Result)
'''
Should not have space after 'print'
'''