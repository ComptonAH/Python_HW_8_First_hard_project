def create_data(path):
    catalog = open(path,'r')
    full_data = catalog.readlines()
    for i in full_data:
        if i == '\n':
            full_data.remove(i)
    return full_data

def search_by_name(data):
    spec_name = input('Enter the name you are looking for: ').lower()
    for index, line in enumerate(data):
        if line.lower().count(spec_name):
            for person in range(index, index+4):
                print('\n'+data[index])
                index +=1

def search_by_surname(data):
    spec_surname = input('Enter the surname you are looking for: ').lower()
    for index, line in enumerate(data):
        if line.lower().count(spec_surname):
            for person in range(index, index+4):
                print('\n'+data[index-1])
                index +=1

def search_by_patronymic(data):
    spec_patronymic = input('Enter the patronymic you are looking for: ').lower()
    for index, line in enumerate(data):
        if line.lower().count(spec_patronymic):
            for person in range(index, index+4):
                print('\n'+data[index-2])
                index +=1

def search_by_phone_number(data):
    spec_phone_number = input('Enter the number via you are looking for (w/o plus symbol "+"): ')
    if spec_phone_number.count('+'):
        print('Please enter the number without "+"')
    else:
        for index, line in enumerate(data):
            if line.lower().count(spec_phone_number):
                for person in range(index, index+4):
                    print('\n'+data[index-3])
                    index +=1

def searching(characheristic, data):
    if characheristic == 'name':
        search_by_name(data)
    elif characheristic == 'surname':
        search_by_surname(data)
    elif characheristic == 'patronymic':
        search_by_patronymic(data)
    elif characheristic == 'phone number':
        search_by_phone_number(data)

def mode_w(path):
    catalog = open(path,mode)
    catalog.close

def mode_a(path):
    catalog = open(path,mode)
    quan_to_add = int(input('Enter the number of persons you want to add: '))
    for i in range(quan_to_add):
        name = input('Enter the name: ').title()
        surname = input('Enter the surname: ').title()
        patronymic = input('Enter the patronymic: ').title()
        phone_num = input('Enter the phone number: ').title()
        data = f'Name: {name}' + '\n' + f'Surname: {surname}' + '\n' + f'Patronymic: {patronymic}' +  '\n' + f'Phone number: {phone_num}' + '\n'
        catalog.write(f'{data}\n')
    catalog.close

def mode_r(path):
    data = create_data(path)
    characheristic = input('Enter the characheristic: ').lower()
    searching(characheristic, data)

def menu_mode(mode, path):
    if mode == 'w':  
        mode_w(path)
    elif mode == 'a':
        mode_a(path)
    elif mode == 'r':
        mode_r(path)
    else:
        print('Enter the one of the specified symbols to get access to the menu!')


path = 'first_task.txt'
mode = input('Enter the mode you want to use: ("a" is adding a new person; "w" is refreshing the whole file; "r" is looking for a person via characheristic)\n')
menu_mode(mode, path)