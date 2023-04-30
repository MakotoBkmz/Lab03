#Expected reuslt should be: My name is David, I am 14 years old👣

# f = '\N{Footprints}'  # not informative naming, the correct code below
smile_footprint = '\N{Footprints}'

# User_ name = input()
user_name = input('Please, enter your name >>> ').title()

# User_age =input ('Please, enter your age >>> ')
user_age = input('Please, enter your age >>> ')

# результат = 'My name is' + User_ name + ", I am" + User_age + 'years old' + smile_footprint
result = f'My name is {user_name}, I am {user_age} years old{smile_footprint}'

# print (результат)
print(result)
